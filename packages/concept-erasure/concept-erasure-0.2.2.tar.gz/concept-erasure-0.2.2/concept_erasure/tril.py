from functools import lru_cache
import math

from torch import Tensor
import torch


@lru_cache
def tril_indices(d: int, device: torch.device | str | None) -> tuple[Tensor, Tensor]:
    """Thin wrapper around `torch.tril_indices` that caches the result."""
    rows, cols = torch.tril_indices(d, d, device=device)
    return rows, cols


def symmetric_to_tril(A: Tensor) -> Tensor:
    """Condense a symmetric matrices to their lower triangular parts."""
    *_, d, d2 = A.shape
    assert d == d2, "Expected a square matrix or batch thereof"

    rows, cols = tril_indices(d, A.device)
    return A[..., rows, cols]


def tril_to_symmetric(tril: Tensor) -> Tensor:
    """Expand condensed lower triangulars into symmetric matrices."""
    *leading, x = tril.shape

    # Deduce the dimension of the original square matrix from x. This means finding
    # the positive root of f(d) = (d^2 + d) / 2 - x, which should be an integer.
    maybe_d = (math.sqrt(8 * x + 1) - 1) / 2
    assert maybe_d.is_integer(), f"No square matrix has {x} tril elements"

    # Create an empty symmetric matrix
    d = int(maybe_d)
    mat = tril.new_empty(*leading, d, d)

    # Fill in the lower triangular part
    rows, cols = torch.tril_indices(d, d, device=tril.device)
    mat[..., rows, cols] = tril

    # Copy the lower triangular part to the upper triangular part
    rows, cols = torch.triu_indices(d, d, device=tril.device)
    mat[..., rows, cols] = mat[..., cols, rows]

    return mat
