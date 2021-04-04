"""
Small game of life core implementation.

The game of life is divided into obtaining the fields around each cell,
updating each cell in a generation, obtaining a new board generation and
evolving the board n generations.
"""

from typing import Literal, Tuple

import numpy as np
from numpy.lib.stride_tricks import as_strided


def generate_fields(
    board: np.array, mode: Literal["wrap", "zeros"] = "wrap"
) -> np.array:
    """Generate fields from board.

    Extract all the (3, 3) fields to calculate the
    field center cell life state. By default, the board is paded in wrap mode
    AKA the board has a toroid form, but can be changed to zeros
    depending in the desired edge behavior.

    Arguments
    ---------
    board: The Game of life board (n, m) where
    n >= 2 and m >= 2

    Returns
    -------
    The fields around each cell of the board. It has a shape of
    (n, m, 3, 3)
    """
    board_shape = board.shape
    assert board_shape[0] >= 2 and board_shape[1] >= 2

    if mode == "zeros":
        padded_board = np.pad(board, (1, 1))
    elif mode == "wrap":
        padded_board = np.pad(board, (1, 1), mode=mode)

    else:
        raise TypeError("Mode not defined.")

    return as_strided(
        padded_board,
        shape=board_shape + (3, 3),
        strides=padded_board.strides + padded_board.strides,
    )


def update_cell(field: np.array) -> int:
    """Set the state of the cell life depending on the field sum.

    1. If the field sums 3, cell is set to living.
    2. Else if the sums equals 4, cell state carries out the same.
    3. Every other results, sets the cell state to death.

    Arguments
    ---------
    field: Neighborhood of cells of shape (3, 3).

    Returns
    -------
    The cell state. 1 to live, 0 to death.
    """
    field_shape = field.shape
    assert field_shape[0] == 3 and field_shape[1] == 3

    total = np.sum(field)
    cell = 0

    if total == 3:
        cell = 1
    elif total == 4:
        cell = field[1][1]

    return cell


def update_board(board: np.array, mode: Literal["wrap", "zeros"] = "wrap") -> np.array:
    """Move one generation in the game of life.

    The operation is inmutable.

    Arguments
    ---------
    board: Game of life board with shape (n, m) where
    n >= 2 and m >= 2

    Returns
    -------
    new board in one generation older with shape (n, m)
    """
    new_board = board.copy()
    board_shape = new_board.shape
    assert board_shape[0] >= 2 and board_shape[1] >= 2

    fields = generate_fields(new_board, mode)

    for i in range(board_shape[0]):
        for j in range(board_shape[1]):
            new_board[i][j] = update_cell(fields[i][j])

    return new_board


def evolve_board(
    board: np.array, n_times: int, mode: Literal["wrap", "zeros"] = "wrap"
) -> np.array:
    """
    Iterate through a board `n` generations.

    Arguments
    ---------
    board: Game of life board with shape (n, m) where
    n >= 2 and m >= 2

    Yields
    ------
    a new board with the state the current generation.
    """
    board_shape = board.shape
    assert board_shape[0] >= 2 and board_shape[1] >= 2

    new_board = board.copy()
    for _ in range(n_times):
        new_board = update_board(new_board, mode)
        yield new_board
