#!/usr/bin/env python3

import re


# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

NUM: re.Pattern = re.compile(r"\b\d+\b")

possibles = 0
with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        sides = [int(s) for s in NUM.findall(line)]
        largest = max(sides)
        if 2 * largest < sum(sides):
            # print(f"possible: {sides}")
            possibles += 1
        else:
            # print(f"impossible: {sides}")
            pass

print(f"\npossibles: {possibles}")
