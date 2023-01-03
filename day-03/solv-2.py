#!/usr/bin/env python3

import re


# INPUT_FILE_NAME: str = "test-input-2"
INPUT_FILE_NAME: str = "input"

NUM: re.Pattern = re.compile(r"\b\d+\b")

possibles = 0
with open(INPUT_FILE_NAME, "r") as input_file:
    lines = []
    for line in input_file:
        lines.append(line)
        if len(lines) != 3:
            continue

        sides_per_line = [[int(s) for s in NUM.findall(line)] for line in lines]
        for col in range(3):
            sides = [sides_per_line[row][col] for row in range(3)]

            largest = max(sides)
            if 2 * largest < sum(sides):
                print(f"possible: {sides}")
                possibles += 1
            else:
                print(f"impossible: {sides}")
                pass

        lines = []

print(f"\npossibles: {possibles}")
