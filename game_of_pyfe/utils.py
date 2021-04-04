"""
Utilities for game of pyfe.
"""
import os
from typing import List

import numpy as np


def cls():
    """Clean the terminal."""
    os.system("cls" if os.name == "nt" else "clear")


def validate_board(board: np.array) -> np.array:
    """Validate the Game of life board.

    Validates that the board cumplies with the following parameters.
    1. Has shape of (n, m).
    2. Only contains 1's (life) and 0's (death).

    Arguments
    ---------
    board: Game of life board.

    Raises
    ------
    TypeError if does not cumply with shape.
    ValueError if does not has only 1's and 0's.

    Returns
    -------
    The original board.
    """
    board_shape = board.shape

    if not (len(board_shape) == 2 and board_shape[0] >= 2 and board_shape[1] >= 2):
        raise TypeError("board does not contain the correct shape")

    for i in range(board_shape[0]):
        for j in range(board_shape[1]):
            if not (board[i][j] == 0 or board[i][j] == 1):
                raise ValueError(
                    "Board contains a {} in index [{}, {}]".format(board[i][j], i, j)
                )

    return board


def create_printable_board(board: np.array) -> List[List[int]]:
    """Format the board to be printed in the terminal.

    For convinience and testability, the array contains the in representing
    'space' for 0's and 'white box' for 1's

    Arguments
    ---------
    board: Game of life board.

    Returns
    -------
    A list containing the lines of integers representing each cell
    life state.
    """
    black_square = 9608
    space = 32

    printable_board = board.copy()

    printable_board[printable_board == 0] = space
    printable_board[printable_board == 1] = black_square

    return printable_board.tolist()
