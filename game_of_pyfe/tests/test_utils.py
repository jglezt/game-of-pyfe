"""
Test suit for utils.py file.
"""
import math

import numpy as np

from ..utils import create_printable_board, validate_board
from .base_test import BaseTestCase, unittest


class TestValidateBoard(BaseTestCase):
    """
    Tests for the validate_board function.
    """

    def test_board_shape(self):
        """Test board shape validation."""
        board = np.zeros([1, 1])
        self.assertRaises(TypeError, validate_board, board)

        board = np.zeros([0, 0])
        self.assertRaises(TypeError, validate_board, board)

        board = np.zeros([2, 0])
        self.assertRaises(TypeError, validate_board, board)

        board = np.zeros([0, 2])
        self.assertRaises(TypeError, validate_board, board)

        board = np.zeros([1])
        self.assertRaises(TypeError, validate_board, board)

        board = np.zeros([2])
        self.assertRaises(TypeError, validate_board, board)

        board = np.zeros([2, 2])
        result = validate_board(board)
        self.assert_array_equal(result, board)

    def test_values_board(self):
        """Test board values validation."""
        board = np.arange(4).reshape((2, 2))
        self.assertRaises(ValueError, validate_board, board)

        board = np.zeros([2, 2])
        board[0, 0] = -1
        self.assertRaises(ValueError, validate_board, board)

        board = np.ones([2, 2])
        result = validate_board(board)
        self.assert_array_equal(result, board)


class TestCreatePrintableBoard(BaseTestCase):
    """
    Tests for the printable_board function.
    """

    def test_base_board(self):
        """Test if correct board is returned."""
        board = np.array(
            [
                [1, 1, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
        expected_result = [
            [9608, 9608, 32, 32, 9608],
            [32, 32, 32, 32, 32],
            [32, 32, 32, 32, 32],
            [32, 32, 32, 32, 32],
            [32, 32, 32, 32, 32],
        ]
        result = create_printable_board(board)
        self.assertCountEqual(result, expected_result)
