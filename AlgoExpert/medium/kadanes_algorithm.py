"https://www.algoexpert.io/questions/kadane's-algorithm"
from typing import List


def kadanes_algorithm(arr: List[int]) -> int:
    # Write your code here.
    sums_at_idx: List[int] = [0 for _ in range(0, len(arr))]

    idx = 0
    while idx < len(arr):
        if idx == 0:
            sums_at_idx[idx] = arr[idx]
            idx += 1
            continue

        sum_at_idx = arr[idx] + sums_at_idx[idx - 1]
        if arr[idx] > sum_at_idx:
            sums_at_idx[idx] = arr[idx]
        else:
            sums_at_idx[idx] = sum_at_idx

        idx += 1

    return max(sums_at_idx)
