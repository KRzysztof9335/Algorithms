"https://www.codingame.com/ide/puzzle/network-cabling"
import statistics
from typing import List


def get_cable_length(axis: int, y_vals: List[int]) -> int:
    length = 0
    for y in y_vals:
        length += abs(axis - y)

    return length


def solution() -> int:
    "Calculate cables and return length of cable"
    x_min = float("inf")
    x_max = float("-inf")
    y_vals: List[int] = []

    for _ in range(int(input())):
        x, y = [int(j) for j in input().split()]
        y_vals.append(y)

        if x > x_max:
            x_max = x
        if x < x_min:
            x_min = x

    y_med = int(statistics.median(y_vals))
    length_y: int = get_cable_length(y_med, y_vals)
    length_x: int = int(abs(x_max - x_min))

    return length_y + length_x


print(str(solution()))
