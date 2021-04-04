"""
Game of pyfe application.

The file does not form part of the game-of-pyfe module, rather it acts
as the frontend of the application.
"""
import argparse
import json
import time
from typing import List

import numpy as np

from game_of_pyfe.core import evolve_board
from game_of_pyfe.utils import cls, create_printable_board, validate_board

parser = argparse.ArgumentParser(description="Game of pyfe application.")
parser.add_argument(
    "--conf-file",
    type=argparse.FileType("r"),
    default="./conf.json",
    help="json configuration file containing the board and\
                     edge behavior mode, generations number and time\
                     delay between generations.",
)

args = parser.parse_args()


def print_board(board: np.array, generation: int, time_delay: float) -> None:
    """Print game of life boards.

    Arguments
    ---------
    board: Game of life board.
    generation: Number of the current generation.
    time_delay: Time to wait between generations. In seconds.
    """
    printable_board = create_printable_board(board)

    cls()
    print("Generation: {}".format(generation))
    for line in printable_board:
        print("".join(chr(char) for char in line))
    time.sleep(time_delay)


def main() -> None:
    config_data = json.load(args.conf_file)
    board = np.array(config_data["board"])
    edge_mode = config_data["edge_mode"]
    time_delay = config_data["time_delay"]
    generations = config_data["generations"]

    board = validate_board(board)

    board_evolver = evolve_board(board, generations, edge_mode)

    print_board(board, 0, time_delay)

    for generation, next_board in enumerate(board_evolver):
        print_board(next_board, generation + 1, time_delay)


if __name__ == "__main__":
    main()
