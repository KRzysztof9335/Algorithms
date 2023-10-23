"https://www.codingame.com/ide/puzzle/the-fall-episode-1"
from typing import List


DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

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

# Two dimensional array of types of room
tunnel_map: List[List[int]] = []

# w: number of columns.
# h: number of rows.
_, h = [int(i) for i in input().split()]
for i in range(h):
    # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    line = map(int, input().split())
    tunnel_map.append(list(line))

# the coordinate along the X axis of the exit (not useful for this first mission, but must be read).
_ = int(input())


# game loop
while True:
    inputs = input().split()
    xi = int(inputs[0])
    yi = int(inputs[1])
    pos = inputs[2]

    room_type = tunnel_map[yi][xi]
    next_move = ROOMS_MOVES[room_type][pos]
    next_x = xi + next_move[0]
    next_y = yi + next_move[1]

    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    print(f"{next_x} {next_y}")
