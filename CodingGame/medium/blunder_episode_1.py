# https://www.codingame.com/training/medium/blunder-episode-1
from typing import Dict, List
import sys

def printd(msg: str):
    print(f"DEBUG: {msg}", file=sys.stderr, flush=True)

DIRECTIONS = ["S", "E", "N", "W"]
DIRECTIONS_MAP = {"S": "SOUTH", "E": "EAST", "N": "NORTH", "W": "WEST"}


class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __eq__(self, other: 'Point') -> bool:  # type: ignore
        return self.x == other.x and self.y == other.y


class CityMap:

    def __init__(self):
        self.grid: List[str] = []
        self.teleports: Dict[int, Point] = {}
        self.booth = Point()

    def add_row(self, row: str):
        self.grid.append(row)

    def set_booth(self, x: int, y: int):
        self.booth.x = x
        self.booth.y = y

    def add_teleport(self, x: int, y: int):
        if not self.teleports:
            self.teleports[0] = Point(x, y)
        else:
            self.teleports[1] = Point(x, y)

    def get_teleport(self, x: int, y: int) -> Point:
        "For given x, y return point where teleport leads to"
        idx_match = 0
        for idx, teleport in self.teleports.items():
            if teleport.x == x and teleport.y == y:
                idx_match = idx
                break
        if idx_match == 1: return Point(self.teleports[0].x, self.teleports[0].y)
        else:  return Point(self.teleports[1].x, self.teleports[1].y)


class Blunder:

    def __init__(self):
        self.pos = Point()
        self.beer_mode = False
        self.invert_mode = False
        self.teleport_mode = False

        self.loop_detected = False
        self.booth_detected = False

        self.move_idx: int = 0
        self.moves = []
        self.visited: Dict[str, int] = {}

    def set_position(self, x: int, y: int):
        self.pos.x = x
        self.pos.y = y

    def process(self, city_map: CityMap):
        if self.pos == city_map.booth:
            self.booth_detected = True
            return

        printd(f"Blunder current position {self.pos.x} {self.pos.y}, value on position '{city_map.grid[self.pos.y][self.pos.x]}'")

        if city_map.grid[self.pos.y][self.pos.x] == " " or \
           city_map.grid[self.pos.y][self.pos.x] == "@":
            self.handle_basic_move(city_map)

        # Handle direction modifier
        elif city_map.grid[self.pos.y][self.pos.x] in "NSEW":
            self.move_idx = DIRECTIONS.index(city_map.grid[self.pos.y][self.pos.x])
            self.handle_basic_move(city_map)

        # Handle teleport
        elif "T" == city_map.grid[self.pos.y][self.pos.x]:
            self.teleport_mode = not self.teleport_mode
            self.handle_teleport_move(city_map)
            self.handle_basic_move(city_map)

        # Handle beer mode
        elif "B" == city_map.grid[self.pos.y][self.pos.x]:
            self.beer_mode = not self.beer_mode
            self.handle_basic_move(city_map)

        # Handle inverter mode
        elif "I" == city_map.grid[self.pos.y][self.pos.x]:
            self.invert_mode = not self.invert_mode
            self.handle_basic_move(city_map)


    def handle_basic_move(self, city_map: CityMap):
        # Continue the same direction
        next_point = self.get_next_point(DIRECTIONS[self.move_idx])
        if self.can_go_to_point(city_map, next_point):
            self.go_to_point(next_point)
            return

        # Move different direction
        if not self.invert_mode:
            self.move_idx = 0
            move_direction = 1
        else:
            self.move_idx = -1
            move_direction = -1

        while True:
            next_point = self.get_next_point(DIRECTIONS[self.move_idx])
            if self.can_go_to_point(city_map, next_point):
                self.go_to_point(next_point)
                break
            self.move_idx += move_direction


    def get_next_point(self, direction: str) -> Point:
        if direction == "S": return Point(self.pos.x, self.pos.y + 1)
        if direction == "N": return Point(self.pos.x, self.pos.y - 1)
        if direction == "E": return Point(self.pos.x + 1, self.pos.y)
        return Point(self.pos.x - 1, self.pos.y)

    def can_go_to_point(self, city_map: CityMap, point: Point) -> bool:
        # printd(f"Checking if can go to {point.x} {point.y} - map is '{city_map.grid[point.y][point.x]}'")
        if city_map.grid[point.y][point.x] == "#":
            return False

        if city_map.grid[point.y][point.x] == "X":
            if not self.beer_mode:
                return False
            else:
                city_map.grid[point.y] = city_map.grid[point.y][0:point.x] + ' ' + city_map.grid[point.y][point.x + 1:]  # type:ignore
                self.reset_moves_loop_count()
                return True
        return True

    def handle_teleport_move(self, city_map: CityMap):
        next_point = city_map.get_teleport(self.pos.x, self.pos.y)
        self.pos = next_point

    def reset_moves_loop_count(self):
        for move_id, _ in self.visited.items():
            self.visited[move_id] = 0

    def go_to_point(self, point: Point):
        move_id = f"{self.pos.x}_{self.pos.y}_{point.x}_{point.y}"
        self.pos = point
        self.moves.append(DIRECTIONS_MAP[DIRECTIONS[self.move_idx]])
        self.visited.setdefault(move_id, 0)
        self.visited[move_id] += 1

        if self.visited[move_id] >= 3:
            self.loop_detected = True
            self.moves = ["LOOP"]


def get_input(city_map: CityMap, blunder: Blunder):

    l, _ = [int(i) for i in input().split()]
    for y in range(l):
        row = input()
        city_map.grid.append(row)

        for x, character in enumerate(row):
            if character == "@":
                blunder.set_position(x, y)
            elif character == "$":
                city_map.set_booth(x, y)
            elif character == "T":
                city_map.add_teleport(x, y)


def solution():
    city_map = CityMap()
    blunder = Blunder()
    get_input(city_map, blunder)

    printd(f"Blunder position {blunder.pos.x} {blunder.pos.y}")
    printd(f"Booth position: {city_map.booth.x} {city_map.booth.y}")

    # for row in city_map.grid:
    #     printd(row)

    while not blunder.booth_detected and not blunder.loop_detected:
        blunder.process(city_map)

    return blunder.moves

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
moves = solution()

for move in moves:
    print(move)