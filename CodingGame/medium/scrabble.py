"https://www.codingame.com/ide/puzzle/scrabble"
from copy import deepcopy
from typing import Dict, List, Tuple

POINTS_TABLE = {"e": 1, "a": 1, "i": 1, "o": 1, "n": 1, "r": 1, "t": 1, " l": 1, "s": 1, "u": 1,
                "d": 2, "g": 2,
                "b":3 , "c": 3, "m": 3, "p": 3,
                "f": 4, "h": 4, "v": 4, "w": 4, "y": 4,
                "k": 5,
                "j": 8, "x": 8,
                "q": 10, "z": 10}


def get_input() -> Tuple[str, List[str]]:
    "Get input"
    words_in_dictionary: List[str] = []
    for _ in range(int(input())):
        words_in_dictionary.append(input())
    letters = input()
    return letters, words_in_dictionary


def calculate_letters(letters: str) -> Dict[str, int]:
    "Calculate each letter"
    out: Dict[str, int] = {}

    for letter in letters:
        out.setdefault(letter, 0)
        out[letter] += 1
    return out


def solution():
    "Calculate solution"
    letters, words = get_input()
    letters = calculate_letters(letters)

    word_best = ""
    word_points_best = 0

    for word in words:
        current_word_points = 0
        correct_word_correct = True
        letters_available = deepcopy(letters)

        # Ignore words larger then available letters
        if len(word) > len(letters_available):
            continue

        for letter in word:
            if letter not in letters_available or not letters_available[letter]:
                correct_word_correct = False
                break
            current_word_points += POINTS_TABLE[letter]
            letters_available[letter] -= 1

        if not correct_word_correct:
            continue

        if current_word_points > word_points_best:
            word_best = word
            word_points_best = current_word_points

        if current_word_points == word_points_best and len(word) < len(word_best):
            word_best = word
            word_points_best = current_word_points

    return word_best

print(solution())
