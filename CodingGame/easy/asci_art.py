"""https://www.codingame.com/training/easy/ascii-art"""
from typing import List
L = int(input())
H = int(input())
letters = list(input())

T: List[List[str]] = []
for i in range(H):
    T.append(list(input()))


def solution():
    "Solution"
    for row, _ in enumerate(T):
        row_string = ""
        for letter in letters:
            letter_idx = 26
            if letter.isalpha():
                letter_idx = ord(letter.capitalize()) - 65
            row_idx_start = letter_idx * L
            row_idx_end = letter_idx * L + L
            row_string += "".join(T[row][row_idx_start:row_idx_end])
        print(''.join(row_string))


solution()
