# Game of Pyfe

Simple python implementation of Conway's Game of Life
[Reference](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

## Installation
To install the module, download this repository.
```
git clone https://github.com/jglezt/game-of-pyfe.git
```

Then install the module using pip.
```
pip install .
```

## Requirements
1. python >= 3.8

## Quick start
To run the application, run the file `game_of_pyfe.py`
```
python game_of_pyfe.py
```

It will display a simple spaceship evolution through 10 generations in a toroid grid of 5 by 5.


## Tests
To run the module tests:
```
python -m pytest
```

## Description
The code is divided into two. First, the module game-of-pyfe that implements the logic of Conway's Game of Life in a finite board. And finally the front end `game_of_pyfe.py` where the user can interact with the implementation.
The rationale behind this decision is to have a module that could be used with any TUI front end implementation or any other application that requires the Game of life logic.

### Front end
```
usage: game_of_pyfe.py [-h] [--conf-file CONF_FILE]

Game of pyfe application.

optional arguments:
  -h, --help            show this help message and exit
  --conf-file CONF_FILE
                        json configuration file containing the board and edge behavior mode,
                        iterations number and time delay between generations.
```

The front end has only one argument, the configuration file location.

### conf.json file
In conf.json, the user describes the initial board, how the edges logic will be handle, the delay between each generation and the number of generations to reproduce.
In total, there is 4 configurable variables that are described as follows:

1. `board`: Contains the desired pattern and size of the initial board. '1' represents the state of life while `0` represents a lifeless cell. The shape of the board should be `(n, m)` and no other number other than `1` and `0` should be use to represent the board.
2. `time_delay`: In seconds, represents how much time the board is printed in the terminal.
3. `generations`: Contains how many iterations should the program run.
4. `edge_mode`: Indicates what lays beyond the edges of the board. For `wrap`, the next cell beyond the edge is the opposite from the other side of the board. Finally, `zeros` sets the next cell beyond the edge to `0` (lifeless cell).
