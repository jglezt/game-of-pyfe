"""
Test suit for core.py file.
"""
import math

import numpy as np

from ..core import evolve_board, generate_fields, update_board, update_cell
from .base_test import BaseTestCase, unittest


class TestGenerateFields(BaseTestCase):
    """
    Tests for the generate_fields function.
    """

    def test_exception_raising(self):
        """Test  when board is smaller than 2 in any of the axis."""
        board = np.zeros([1, 1])
        self.assertRaises(AssertionError, generate_fields, board)

        board = np.zeros([0, 0])
        self.assertRaises(AssertionError, generate_fields, board)

        board = np.zeros([2, 0])
        self.assertRaises(AssertionError, generate_fields, board)

        board = np.zeros([0, 2])
        self.assertRaises(AssertionError, generate_fields, board)

        board = np.zeros([1])
        self.assertRaises(AssertionError, generate_fields, board)

        # Does not need an spetial assert, it could be assumed from
        # the IndexError exception
        board = np.zeros([2])
        self.assertRaises(IndexError, generate_fields, board)

        # When the mode does not exist
        board = np.zeros([2, 2])
        self.assertRaises(TypeError, generate_fields, board, "nil")

    def test_base_case(self):
        """Test using boards of size n == m."""
        board = np.arange(4).reshape((2, 2))
        expected_result = np.array(
            [
                [[[3, 2, 3], [1, 0, 1], [3, 2, 3]], [[2, 3, 2], [0, 1, 0], [2, 3, 2]]],
                [[[1, 0, 1], [3, 2, 3], [1, 0, 1]], [[0, 1, 0], [2, 3, 2], [0, 1, 0]]],
            ]
        )

        result = generate_fields(board)

        self.assert_array_equal(result, expected_result)

        board = np.arange(9).reshape((3, 3))
        expected_result = np.array(
            [
                [
                    [[8, 6, 7], [2, 0, 1], [5, 3, 4]],
                    [[6, 7, 8], [0, 1, 2], [3, 4, 5]],
                    [[7, 8, 6], [1, 2, 0], [4, 5, 3]],
                ],
                [
                    [[2, 0, 1], [5, 3, 4], [8, 6, 7]],
                    [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
                    [[1, 2, 0], [4, 5, 3], [7, 8, 6]],
                ],
                [
                    [[5, 3, 4], [8, 6, 7], [2, 0, 1]],
                    [[3, 4, 5], [6, 7, 8], [0, 1, 2]],
                    [[4, 5, 3], [7, 8, 6], [1, 2, 0]],
                ],
            ]
        )
        result = generate_fields(board)
        self.assert_array_equal(result, expected_result)

    def test_non_equal_axis_boards(self):
        """Test the behaviuor of the generate_fields function when n != m."""
        board = np.arange(6).reshape((3, 2))
        expected_result = np.array(
            [
                [[[5, 4, 5], [1, 0, 1], [3, 2, 3]], [[4, 5, 4], [0, 1, 0], [2, 3, 2]]],
                [[[1, 0, 1], [3, 2, 3], [5, 4, 5]], [[0, 1, 0], [2, 3, 2], [4, 5, 4]]],
                [[[3, 2, 3], [5, 4, 5], [1, 0, 1]], [[2, 3, 2], [4, 5, 4], [0, 1, 0]]],
            ]
        )

        result = generate_fields(board)
        self.assert_array_equal(result, expected_result)

        board = np.arange(6).reshape((2, 3))
        expected_result = np.array(
            [
                [
                    [[5, 3, 4], [2, 0, 1], [5, 3, 4]],
                    [[3, 4, 5], [0, 1, 2], [3, 4, 5]],
                    [[4, 5, 3], [1, 2, 0], [4, 5, 3]],
                ],
                [
                    [[2, 0, 1], [5, 3, 4], [2, 0, 1]],
                    [[0, 1, 2], [3, 4, 5], [0, 1, 2]],
                    [[1, 2, 0], [4, 5, 3], [1, 2, 0]],
                ],
            ]
        )

        result = generate_fields(board)
        self.assert_array_equal(result, expected_result)

    def test_zeros_mode(self):
        """Test the zeros edge pading."""
        board = np.arange(4).reshape((2, 2))
        expected_result = np.array(
            [
                [[[0, 0, 0], [0, 0, 1], [0, 2, 3]], [[0, 0, 0], [0, 1, 0], [2, 3, 0]]],
                [[[0, 0, 1], [0, 2, 3], [0, 0, 0]], [[0, 1, 0], [2, 3, 0], [0, 0, 0]]],
            ]
        )

        result = generate_fields(board, "zeros")

        self.assert_array_equal(result, expected_result)

        board = np.arange(9).reshape((3, 3))
        expected_result = np.array(
            [
                [
                    [[0, 0, 0], [0, 0, 1], [0, 3, 4]],
                    [[0, 0, 0], [0, 1, 2], [3, 4, 5]],
                    [[0, 0, 0], [1, 2, 0], [4, 5, 0]],
                ],
                [
                    [[0, 0, 1], [0, 3, 4], [0, 6, 7]],
                    [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
                    [[1, 2, 0], [4, 5, 0], [7, 8, 0]],
                ],
                [
                    [[0, 3, 4], [0, 6, 7], [0, 0, 0]],
                    [[3, 4, 5], [6, 7, 8], [0, 0, 0]],
                    [[4, 5, 0], [7, 8, 0], [0, 0, 0]],
                ],
            ]
        )

        result = generate_fields(board, "zeros")

        self.assert_array_equal(result, expected_result)


class TestUpdateCell(BaseTestCase):
    """
    Tests for the update_cell function.
    """

    def test_exception_raising(self):
        """Test for fields of shape different from (3, 3)."""
        field = np.zeros((2, 3))

        self.assertRaises(AssertionError, update_cell, field)

        field = np.zeros((3, 2))

        self.assertRaises(AssertionError, update_cell, field)

        field = np.zeros((2, 2))

        self.assertRaises(AssertionError, update_cell, field)

        # Does not need an spetial assert, it could be assumed from
        # the IndexError exception
        field = np.zeros([3])
        self.assertRaises(IndexError, update_cell, field)

    def test_life_status(self):
        """Test for the life status, when the total sum of the field\
        equals 3."""
        field = np.zeros([3, 3])
        field[1, 1] = 1
        field[2, 2] = 1
        field[0, 0] = 1

        self.assertEqual(1, update_cell(field))

        field = np.zeros([3, 3])
        field[0, 1] = 1
        field[0, 2] = 1
        field[0, 0] = 1

        self.assertEqual(1, update_cell(field))

    def test_equal_state(self):
        """Test if the function returns the same state as the field\
        center cell when sum of field equals 4."""
        field = np.zeros([3, 3])
        field[1, 1] = 1
        field[2, 2] = 1
        field[0, 0] = 1
        field[1, 0] = 1

        self.assertEqual(field[1, 1], update_cell(field))

        field = np.zeros([3, 3])
        field[1, 1] = 0
        field[2, 2] = 1
        field[0, 0] = 1
        field[1, 0] = 1
        field[0, 1] = 1

        self.assertEqual(field[1, 1], update_cell(field))

    def test_death_state(self):
        """Test death state for any every other sum result."""
        field = np.ones([3, 3])

        self.assertEqual(0, update_cell(field))

        field = np.zeros([3, 3])
        self.assertEqual(0, update_cell(field))


class TestUpdateBoard(BaseTestCase):
    """
    Tests for the update_board function.
    """

    def test_exception_raising(self):
        """Test for fields of shape different from (3, 3)."""
        board = np.zeros([1, 1])
        self.assertRaises(AssertionError, update_board, board)

        board = np.zeros([0, 0])
        self.assertRaises(AssertionError, update_board, board)

        board = np.zeros([2, 0])
        self.assertRaises(AssertionError, update_board, board)

        board = np.zeros([0, 2])
        self.assertRaises(AssertionError, update_board, board)

        board = np.zeros([1])
        self.assertRaises(AssertionError, update_board, board)

        # Does not need an spetial assert, it could be assumed from
        # the IndexError exception
        board = np.zeros([2])
        self.assertRaises(IndexError, update_board, board)

    def test_oscillator(self):
        """Test if the function correctly produces the next\
        step of a simple oscillator."""
        board = np.array(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
        expected_result = np.array(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
        result = update_board(board)

        self.assert_array_equal(result, expected_result)

    def test_oscillator_edge_wrap(self):
        """Test simple oscillator in edge."""
        board = np.array(
            [
                [1, 1, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
        expected_result = np.array(
            [
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
            ]
        )
        result = update_board(board)

        self.assert_array_equal(result, expected_result)

    def test_oscillator_edge_zeros(self):
        """Test simple oscillator in edge using zeros padding."""
        board = np.array(
            [
                [1, 1, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
        expected_result = np.array(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
        result = update_board(board, "zeros")

        self.assert_array_equal(result, expected_result)


class TestEvolveBoard(BaseTestCase):
    """
    Tests for the evolve_board function.
    """

    def test_exception_raising(self):
        """Test  when board is smaller than 2 in any of the axis."""
        board = np.zeros([1, 1])
        iterator = evolve_board(board, 1)
        self.assertRaises(AssertionError, iterator.__next__)

        board = np.zeros([0, 0])
        iterator = evolve_board(board, 1)
        self.assertRaises(AssertionError, iterator.__next__)

        board = np.zeros([2, 0])
        iterator = evolve_board(board, 1)
        self.assertRaises(AssertionError, iterator.__next__)

        board = np.zeros([0, 2])
        iterator = evolve_board(board, 1)
        self.assertRaises(AssertionError, iterator.__next__)

        board = np.zeros([1])
        iterator = evolve_board(board, 1)
        self.assertRaises(AssertionError, iterator.__next__)

        # Does not need an spetial assert, it could be assumed from
        # the IndexError exception
        board = np.zeros([2])
        iterator = evolve_board(board, 1)
        self.assertRaises(IndexError, iterator.__next__)

    def test_zero_generations(self):
        """Test if the generator stops when 0 generations are given."""
        board = np.zeros([3, 3])
        iterator = evolve_board(board, 0)
        self.assertRaises(StopIteration, iterator.__next__)

    def test_simplespaceship(self):
        """Test if the function can reproduce a simple spaceship\
         through one generation."""
        board = np.array(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0],
            ]
        )
        expected_results = [
            np.array(
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 1, 0, 1, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 1, 0, 0],
                ]
            ),
            np.array(
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 1, 0],
                    [0, 0, 1, 1, 0],
                ]
            ),
        ]
        next_boards = evolve_board(board, 2)

        for next_board, expected_result in zip(next_boards, expected_results):
            self.assert_array_equal(next_board, expected_result)
