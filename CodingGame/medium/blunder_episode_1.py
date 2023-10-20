"https://www.codingame.com/training/medium/blunder-episode-1"
from typing import Dict, List
import sys


def printd(msg: str):
    print(f"DEBUG: {msg}", file=sys.stderr, flush=True)


DIRECTIONS = ["S", "E", "N", "W"]
DIRECTIONS_MAP = {"S": "SOUTH", "E": "EAST", "N": "NORTH", "W": "WEST"}


class Point:  # pylint: disable=too-few-public-methods
    def __init__(self, pos_x: int = 0, pos_y: int = 0):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def __eq__(self, other: 'Point') -> bool:  # type: ignore
        return self.pos_x == other.pos_x and self.pos_y == other.pos_y


class CityMap:
    def __init__(self):
        self.grid: List[str] = []
        self.teleports: Dict[int, Point] = {}
        self.booth = Point()

    def add_row(self, row: str):
        self.grid.append(row)

    def set_booth(self, pos_x: int, pos_y: int):
        self.booth.pos_x = pos_x
        self.booth.pos_y = pos_y

    def add_teleport(self, pos_x: int, pos_y: int):
        if not self.teleports:
            self.teleports[0] = Point(pos_x, pos_y)
        else:
            self.teleports[1] = Point(pos_x, pos_y)

    def get_teleport(self, pos_x: int, pos_y: int) -> Point:
        "For given x, y return point where teleport leads to"
        idx_match = 0
        for idx, teleport in self.teleports.items():
            if teleport.pos_x == pos_x and teleport.pos_y == pos_y:
                idx_match = idx
                break
        if idx_match == 1:
            return Point(self.teleports[0].pos_x, self.teleports[0].pos_y)
        return Point(self.teleports[1].pos_x, self.teleports[1].pos_y)


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

    def set_position(self, pos_x: int, pos_y: int):
        self.pos.pos_x = pos_x
        self.pos.pos_y = pos_y

    def process(self, city_map: CityMap):
        if self.pos == city_map.booth:
            self.booth_detected = True
            return

        if city_map.grid[self.pos.pos_y][self.pos.pos_x] == " " or \
           city_map.grid[self.pos.pos_y][self.pos.pos_x] == "@":
            self.handle_basic_move(city_map)

        # Handle direction modifier
        elif city_map.grid[self.pos.pos_y][self.pos.pos_x] in "NSEW":
            self.move_idx = DIRECTIONS.index(city_map.grid[self.pos.pos_y][self.pos.pos_x])
            self.handle_basic_move(city_map)

        # Handle teleport
        elif city_map.grid[self.pos.pos_y][self.pos.pos_x] == "T":
            self.teleport_mode = not self.teleport_mode
            self.handle_teleport_move(city_map)
            self.handle_basic_move(city_map)

        # Handle beer mode
        elif city_map.grid[self.pos.pos_y][self.pos.pos_x] == "B":
            self.beer_mode = not self.beer_mode
            self.handle_basic_move(city_map)

        # Handle inverter mode
        elif city_map.grid[self.pos.pos_y][self.pos.pos_x] == "I":
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
        if direction == "S":
            return Point(self.pos.pos_x, self.pos.pos_y + 1)
        if direction == "N":
            return Point(self.pos.pos_x, self.pos.pos_y - 1)
        if direction == "E":
            return Point(self.pos.pos_x + 1, self.pos.pos_y)
        return Point(self.pos.pos_x - 1, self.pos.pos_y)

    def can_go_to_point(self, city_map: CityMap, point: Point) -> bool:
        if city_map.grid[point.pos_y][point.pos_x] == "#":
            return False

        if city_map.grid[point.pos_y][point.pos_x] == "X":
            if not self.beer_mode:
                return False
            city_map.grid[point.pos_y] = city_map.grid[point.pos_y][0:point.pos_x] + ' ' + \
                city_map.grid[point.pos_y][point.pos_x + 1:]
            self.reset_moves_loop_count()
            return True
        return True

    def handle_teleport_move(self, city_map: CityMap):
        next_point = city_map.get_teleport(self.pos.pos_x, self.pos.pos_y)
        self.pos = next_point

    def reset_moves_loop_count(self):
        for move_id, _ in self.visited.items():
            self.visited[move_id] = 0

    def go_to_point(self, point: Point):
        move_id = f"{self.pos.pos_x}_{self.pos.pos_y}_{point.pos_x}_{point.pos_y}"
        self.pos = point
        self.moves.append(DIRECTIONS_MAP[DIRECTIONS[self.move_idx]])
        self.visited.setdefault(move_id, 0)
        self.visited[move_id] += 1

        if self.visited[move_id] >= 3:
            self.loop_detected = True
            self.moves = ["LOOP"]


def get_input(city_map: CityMap, blunder: Blunder):
    "Get input"
    city_line, _ = [int(i) for i in input().split()]
    for pos_y in range(city_line):
        row = input()
        city_map.grid.append(row)

        for pos_x, character in enumerate(row):
            if character == "@":
                blunder.set_position(pos_x, pos_y)
            elif character == "$":
                city_map.set_booth(pos_x, pos_y)
            elif character == "T":
                city_map.add_teleport(pos_x, pos_y)


def solution():
    "Calculate moves solution"
    city_map = CityMap()
    blunder = Blunder()
    get_input(city_map, blunder)

    while not blunder.booth_detected and not blunder.loop_detected:
        blunder.process(city_map)

    return blunder.moves


for move in solution():
    print(move)
