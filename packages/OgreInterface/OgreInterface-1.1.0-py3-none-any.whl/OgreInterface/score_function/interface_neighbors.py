from typing import Optional, Dict
import torch.nn as nn
import torch


class TransformException(Exception):
    pass


class Transform(nn.Module):
    """
    Base class for all transforms.
    The base class ensures that the reference to the data and datamodule attributes are
    initialized.
    Transforms can be used as pre- or post-processing layers.
    They can also be used for other parts of a model, that need to be
    initialized based on data.
    To implement a new transform, override the forward method. Preprocessors are applied
    to single examples, while postprocessors operate on batches. All transforms should
    return a modified `inputs` dictionary.
    """

    def datamodule(self, value):
        """
        Extract all required information from data module automatically when using
        PyTorch Lightning integration. The transform should also implement a way to
        set these things manually, to make it usable independent of PL.
        Do not store the datamodule, as this does not work with torchscript conversion!
        """
        pass

    def forward(
        self,
        inputs: Dict[str, torch.Tensor],
    ) -> Dict[str, torch.Tensor]:
        raise NotImplementedError

    def teardown(self):
        pass


class NeighborListTransform(Transform):
    """
    Base class for neighbor lists.
    """

    is_preprocessor: bool = True
    is_postprocessor: bool = False

    def __init__(
        self,
        cutoff: float,
    ):
        """
        Args:
            cutoff: Cutoff radius for neighbor search.
        """
        super().__init__()
        self._cutoff = cutoff

    def forward(
        self,
        inputs: Dict[str, torch.Tensor],
    ) -> Dict[str, torch.Tensor]:
        Z = inputs["Z"]
        R = inputs["R"]
        cell = inputs["cell"].view(3, 3)
        pbc = inputs["pbc"]

        idx_i, idx_j, offset = self._build_neighbor_list(
            Z, R, cell, pbc, self._cutoff
        )
        inputs["idx_i"] = idx_i.detach()
        inputs["idx_j"] = idx_j.detach()
        inputs["offsets"] = offset
        return inputs

    def _build_neighbor_list(
        self,
        Z: torch.Tensor,
        positions: torch.Tensor,
        cell: torch.Tensor,
        pbc: torch.Tensor,
        cutoff: float,
    ):
        """Override with specific neighbor list implementation"""
        raise NotImplementedError


class TorchInterfaceNeighborList(NeighborListTransform):
    """
    Environment provider making use of neighbor lists as implemented in TorchAni
    Supports cutoffs and PBCs and can be performed on either CPU or GPU.
    References:
        https://github.com/aiqm/torchani/blob/master/torchani/aev.py
    """

    def _build_neighbor_list(self, Z, positions, cell, pbc, cutoff):
        # Check if shifts are needed for periodic boundary conditions
        if torch.all(pbc == 0):
            shifts = torch.zeros(0, 3, device=cell.device, dtype=torch.long)
        else:
            shifts = self._get_shifts(cell, pbc, cutoff)
        idx_i, idx_j, offset = self._get_neighbor_pairs(
            positions, cell, shifts, cutoff
        )

        # Create bidirectional id arrays, similar to what the ASE neighbor_list returns
        bi_idx_i = torch.cat((idx_i, idx_j), dim=0)
        bi_idx_j = torch.cat((idx_j, idx_i), dim=0)

        # Sort along first dimension (necessary for atom-wise pooling)
        sorted_idx = torch.argsort(bi_idx_i)
        idx_i = bi_idx_i[sorted_idx]
        idx_j = bi_idx_j[sorted_idx]

        bi_offset = torch.cat((-offset, offset), dim=0)
        offset = bi_offset[sorted_idx]
        offset = torch.mm(offset.to(cell.dtype), cell)

        return idx_i, idx_j, offset

    def _get_neighbor_pairs(self, positions, cell, shifts, cutoff):
        """Compute pairs of atoms that are neighbors
        Copyright 2018- Xiang Gao and other ANI developers
        (https://github.com/aiqm/torchani/blob/master/torchani/aev.py)
        Arguments:
            positions (:class:`torch.Tensor`): tensor of shape
                (molecules, atoms, 3) for atom coordinates.
            cell (:class:`torch.Tensor`): tensor of shape (3, 3) of the three vectors
                defining unit cell: tensor([[x1, y1, z1], [x2, y2, z2], [x3, y3, z3]])
            shifts (:class:`torch.Tensor`): tensor of shape (?, 3) storing shifts
        """
        num_atoms = positions.shape[0]
        all_atoms = torch.arange(num_atoms, device=cell.device)

        # 1) Central cell
        pi_center, pj_center = torch.combinations(all_atoms).unbind(-1)
        shifts_center = shifts.new_zeros(pi_center.shape[0], 3)

        # 2) cells with shifts
        # shape convention (shift index, molecule index, atom index, 3)
        num_shifts = shifts.shape[0]
        all_shifts = torch.arange(num_shifts, device=cell.device)
        shift_index, pi, pj = torch.cartesian_prod(
            all_shifts, all_atoms, all_atoms
        ).unbind(-1)
        shifts_outside = shifts.index_select(0, shift_index)

        # 3) combine results for all cells
        shifts_all = torch.cat([shifts_center, shifts_outside])
        pi_all = torch.cat([pi_center, pi])
        pj_all = torch.cat([pj_center, pj])

        # 4) Compute shifts and distance vectors
        # shift_values = torch.mm(shifts_all.to(cell.dtype), cell)
        # Rij_all = positions[pi_all] - positions[pj_all] + shift_values

        # 5) Compute distances, and find all pairs within cutoff
        # distances = torch.norm(Rij_all, dim=1)
        # in_cutoff = torch.nonzero(distances < cutoff, as_tuple=False)

        # 6) Reduce tensors to relevant components
        # pair_index = in_cutoff.squeeze()
        # atom_index_i = pi_all[pair_index]
        # atom_index_j = pj_all[pair_index]
        # offsets = shifts_all[pair_index]

        return pi_all, pj_all, shifts_all
        # return atom_index_i, atom_index_j, offsets

    def _get_shifts(self, cell, pbc, cutoff):
        """Compute the shifts of unit cell along the given cell vectors to make it
        large enough to contain all pairs of neighbor atoms with PBC under
        consideration.
        Copyright 2018- Xiang Gao and other ANI developers
        (https://github.com/aiqm/torchani/blob/master/torchani/aev.py)
        Arguments:
            cell (:class:`torch.Tensor`): tensor of shape (3, 3) of the three
            vectors defining unit cell: tensor([[x1, y1, z1], [x2, y2, z2], [x3, y3, z3]])
            pbc (:class:`torch.Tensor`): boolean vector of size 3 storing
                if pbc is enabled for that direction.
        Returns:
            :class:`torch.Tensor`: long tensor of shifts. the center cell and
                symmetric cells are not included.
        """
        reciprocal_cell = cell.inverse().t()
        inverse_lengths = torch.norm(reciprocal_cell, dim=1)

        num_repeats = torch.ceil(cutoff * inverse_lengths).long()
        num_repeats = torch.where(
            pbc, num_repeats, torch.Tensor([0], device=cell.device).long()
        )

        # This change adds an extra repeat in the x and y direction meaning that the neigbors only need to be applied once
        r1 = torch.arange(1, num_repeats[0] + 2, device=cell.device)
        r2 = torch.arange(1, num_repeats[1] + 2, device=cell.device)
        r3 = torch.arange(1, num_repeats[2] + 1, device=cell.device)
        o = torch.zeros(1, dtype=torch.long, device=cell.device)

        return torch.cat(
            [
                torch.cartesian_prod(r1, r2, r3),
                torch.cartesian_prod(r1, r2, o),
                torch.cartesian_prod(r1, r2, -r3),
                torch.cartesian_prod(r1, o, r3),
                torch.cartesian_prod(r1, o, o),
                torch.cartesian_prod(r1, o, -r3),
                torch.cartesian_prod(r1, -r2, r3),
                torch.cartesian_prod(r1, -r2, o),
                torch.cartesian_prod(r1, -r2, -r3),
                torch.cartesian_prod(o, r2, r3),
                torch.cartesian_prod(o, r2, o),
                torch.cartesian_prod(o, r2, -r3),
                torch.cartesian_prod(o, o, r3),
            ]
        )


if __name__ == "__main__":
    pass
