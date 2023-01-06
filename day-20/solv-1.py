#!/usr/bin/env python3

from typing import List, Tuple

INPUT_FILE_NAME: str = "test-input"
# INPUT_FILE_NAME: str = "input"


def solve(limit: int, ranges: List[Tuple[int, int]]) -> None:
    guess = 0
    range_idx = 0
    while (
        range_idx < len(ranges)
        and ranges[range_idx][0] <= guess <= ranges[range_idx][1]
    ):
        guess = ranges[range_idx][1] + 1
        if guess > limit:
            print("no solution")
            return
        range_idx += 1
        while range_idx < len(ranges) and ranges[range_idx][1] < guess:
            range_idx += 1
    print(guess)


with open(INPUT_FILE_NAME, "r") as input_file:
    limit = int(input_file.readline().strip())
    ranges = [tuple([int(x) for x in line.strip().split("-")]) for line in input_file]
    solve(limit, sorted(ranges))
