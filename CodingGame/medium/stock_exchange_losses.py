"https://www.codingame.com/ide/puzzle/stock-exchange-losses"
from typing import List


def get_input() -> List[int]:
    "Get input"
    _ = int(input())
    out: List[int] = []
    for i in input().split():
        out.append(int(i))
    return out


def solution() -> int:
    "Calculate solution"
    values = get_input()

    previous_max = values[0]
    previous_loss = 0

    for value in values[1:]:
        if value > previous_max:
            previous_max = value

        if value < previous_max:
            current_loss = value - previous_max
            if current_loss < previous_loss:
                previous_loss = current_loss

    return previous_loss


print(str(solution()))
