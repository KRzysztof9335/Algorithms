from typing import List
from hard.dijkstras_algorithm import dijkstrasAlgorithm


def test_case_1_simple_1():
    start = 0
    edges = [[[1, 7]],
             [[2, 6], [3, 20], [4, 3]],
             [[3, 14]],
             [[4, 2]],
             [],
             []]
    assert dijkstrasAlgorithm(start, edges) == [0, 7, 13, 27, 10, -1]


def test_case_2_no_connections():
    start = 1
    edges: List[List[List[int]]] = [[],
                                    [],
                                    [],
                                    []]

    assert dijkstrasAlgorithm(start, edges) == [-1, 0, -1, -1]


def test_case_3_traverse_order_matters():
    start = 7
    edges = [[[1, 1], [3, 1]],
             [[2, 1]],
             [[6, 1]],
             [[1, 3], [2, 4], [4, 2], [5, 3], [6, 5]],
             [[5, 1]],
             [[4, 1]],
             [[5, 2]],
             [[0, 7]]]

    assert dijkstrasAlgorithm(start, edges) == [7, 8, 9, 8, 10, 11, 10, 0]

def test_case_4_recursion():
    start = 0
    edges = [[[1, 1],[7, 8]],
            [[2, 1]],
            [[3, 1]],
            [[4, 1]],
            [[5, 1]],
            [[6, 1]],
            [[7, 1]],
            []]

    assert dijkstrasAlgorithm(start, edges) == [0, 1, 2, 3, 4, 5, 6, 7]