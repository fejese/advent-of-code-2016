#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"


DS = [1j, 1, -1j, -1]


def solve(line: str) -> int:
    di = 0
    pos = 0j
    for step in line.strip().split(", "):
        # print(pos)
        if step.startswith("L"):
            di = (di - 1) % 4
        else:
            di = (di + 1) % 4

        pos += int(step[1:]) * DS[di]

    return int(abs(pos.imag) + abs(pos.real))


with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        print(solve(line))
