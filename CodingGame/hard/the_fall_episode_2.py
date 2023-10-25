"https://www.codingame.com/ide/puzzle/the-fall-episode-1"
from copy import deepcopy
from dataclasses import dataclass
from typing import Any, List, Set, Tuple
import sys

# =================================================================================================
# Constants


DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


# Key is room type. Value is dict, which keys are directions Indie comes in.
ROOMS_MOVES = {
    1: {"TOP": DOWN, "LEFT": DOWN, "RIGHT": DOWN},
    2: {"RIGHT": LEFT, "LEFT": RIGHT},
    3: {"TOP": DOWN},
    4: {"TOP": LEFT, "RIGHT": DOWN},
    5: {"TOP": RIGHT, "LEFT": DOWN},
    6: {"RIGHT": LEFT, "LEFT": RIGHT},
    7: {"TOP": DOWN, "RIGHT": DOWN},
    8: {"LEFT": DOWN, "RIGHT": DOWN},
    9: {"TOP": DOWN, "LEFT": DOWN},
    10: {"TOP": LEFT},
    11: {"TOP": RIGHT},
    12: {"RIGHT": DOWN},
    13: {"LEFT": DOWN}}


# Key is room type. Value is dict defining what will be the room type after rotate
ROOMS_ROTATIONS = {
    1: {"LEFT": 1, "RIGHT": 1},
    2: {"LEFT": 3, "RIGHT": 3},
    3: {"LEFT": 2, "RIGHT": 2},
    4: {"LEFT": 5, "RIGHT": 5},
    5: {"LEFT": 4, "RIGHT": 4},
    6: {"LEFT": 9, "RIGHT": 7},
    7: {"LEFT": 6, "RIGHT": 8},
    8: {"LEFT": 7, "RIGHT": 9},
    9: {"LEFT": 8, "RIGHT": 6},
    10: {"LEFT": 13, "RIGHT": 11},
    11: {"LEFT": 10, "RIGHT": 12},
    12: {"LEFT": 11, "RIGHT": 13},
    13: {"LEFT": 12, "RIGHT": 10}}

# =================================================================================================


def printd(msg: Any):
    print(f"DEBUG: {msg}", file=sys.stderr, flush=True)  # type:ignore


@dataclass
class Position():
    x: int
    y: int
    pos: str


class TunnelMap():
    def __init__(self, width: int, high: int):
        self.width: int = width
        self.high: int = high
        self.grid: List[List[int]] = []
        self.not_rotatable_fields: Set[Tuple[int, int]] = set()

        self.exit = (-1, high)

        self._current_row: int = -1

    def append_row(self, row: List[int]):
        "Append row to existing map"
        self._current_row += 1
        to_add: List[int] = []

        # Add protection if someone tries to append row
        if self._current_row >= self.high:
            raise ValueError("Exceeded number of rows ...")

        # Filter also fields we cannot rotate
        for idx, field in enumerate(row):
            if field < 0:
                self.not_rotatable_fields.add((idx, self._current_row))
            to_add.append(abs(field))
        self.grid.append(to_add)

    def set_exit(self, x: int):
        self.exit = (x, self.high)

    def rotate(self, x: int, y: int, direction: str):
        if direction not in ["LEFT", "RIGHT"]:
            ValueError("Cannot rotate ...")
        old_type = self.grid[y][x]
        self.grid[y][x] = ROOMS_ROTATIONS[old_type][direction]

    def add_rocks(self, rocks: List[Position]):
        "Add rocks which means rooms are no longer rotatable"
        for rock in rocks:
            self.not_rotatable_fields.add((rock.x, rock.y))

# =================================================================================================

def calculate_path(tunnel):
    return []


def play_turn(tunnel_map: TunnelMap, indie: Position, rocks: List[Position]) -> str:
    move = "WAIT"

    new_map = deepcopy(tunnel_map)
    new_map.add_rocks(rocks)

    simulations = []

    # Set limit for now to avoid infinite loop
    idx = 0
    while (indie.x, indie.y) is not tunnel_map.exit:
        idx += 1
        printd(f"Simulating move {idx}")

        # calculate Indie path (till next tile is broken WAIT)

        if idx >= 100:
            break

    return move



# =================================================================================================
# Read input map
# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in input().split()]
tunnel_map = TunnelMap(w, h)
for i in range(h):
    row = list(map(int, input().split()))
    tunnel_map.append_row(row)
ex = int(input())  # the coordinate along the X axis of the exit.
tunnel_map.set_exit(ex)

printd(tunnel_map.grid)
printd(tunnel_map.not_rotatable_fields)

# game loop
while True:
    inputs = input().split()
    xi = int(inputs[0])
    yi = int(inputs[1])
    pos_i = inputs[2]
    indie = Position(xi, yi, pos_i)

    rocks: List[Position] = []
    r = int(input())  # the number of rocks currently in the grid.
    for i in range(r):
        inputs = input().split()
        xr = int(inputs[0])
        yr = int(inputs[1])
        pos_r = inputs[2]
        rocks.append(Position(xr, yr, pos_r))

    next_move = play_turn(tunnel_map, indie, rocks)

    # One line containing on of three commands: 'X Y LEFT', 'X Y RIGHT' or 'WAIT'
    print(next_move)
