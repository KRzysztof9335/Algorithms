"https://www.codingame.com/ide/puzzle/the-gift"
from typing import List, Tuple


def get_input() -> Tuple[int, List[int]]:
    "Collect input"
    contributors_number = int(input())
    to_contribute = int(input())
    budgets: List[int] = []
    for _ in range(contributors_number):
        budgets.append(int(input()))
    return to_contribute, budgets


def solution():
    "Calculate solution"
    to_contribute, budgets = get_input()
    budgets: List[int] = sorted(budgets, reverse=True)
    to_contribute_remaining = to_contribute

    contributions: List[int] = []
    while budgets:
        medium = to_contribute_remaining // len(budgets)

        if medium > budgets[-1]:
            contribution = budgets[-1]
        else:
            contribution = medium

        to_contribute_remaining -= contribution
        contributions.append(contribution)
        budgets.pop()

    return 'IMPOSSIBLE' if to_contribute_remaining else '\n'.join(map(str, contributions))


print(solution())
