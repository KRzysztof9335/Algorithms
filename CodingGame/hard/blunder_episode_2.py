""" https://www.codingame.com/training/hard/blunder-episode-2"""
from dataclasses import dataclass
from typing import Dict

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


@dataclass
class Room:
    "left and right door are ids to next rooms. If exit then value set to -1"
    id: int
    value: int
    left: int
    right: int


def get_input() -> Dict[int, Room]:
    rooms: Dict[int, Room] = {}
    for _ in range(int(input())):
        room = input().split()
        room_id = int(room[0])
        value = int(room[1])
        door_1 = -1 if "E" in room[2] else int(room[2])
        door_2 = -1 if "E" in room[3] else int(room[3])
        rooms[room_id] = Room(int(room_id), value, door_1, door_2)
    return rooms


def solution() -> int:
    rooms = get_input()
    return traverse(rooms, {}, rooms[0])


def traverse(rooms: Dict[int, Room], visited: Dict[int, int], room: Room) -> int:
    amount: int = 0

    if room.id in visited:
        return visited[room.id]

    if room.id == -1:
        visited[room.id] = amount
        return amount

    amount += rooms[room.id].value
    path_left_value = 0 if room.left == -1 else traverse(rooms, visited, rooms[room.left])
    path_right_value = 0 if room.right == -1 else traverse(rooms, visited, rooms[room.right])

    if path_left_value > path_right_value:
        amount += path_left_value
    else:
        amount += path_right_value

    visited[room.id] = amount
    return amount


print(solution())
