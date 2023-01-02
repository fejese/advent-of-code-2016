#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"


# 1 2 3
# 4 5 6
# 7 8 9
KEYPAD = {(x + y * 1j): y * 3 + x + 1 for x in range(3) for y in range(3)}


def follow(instruction: str, pos: complex) -> complex:
    global KEYPAD
    for step in instruction:
        if step == "U":
            next_pos = pos - 1j
        elif step == "D":
            next_pos = pos + 1j
        elif step == "L":
            next_pos = pos - 1
        elif step == "R":
            next_pos = pos + 1
        if next_pos in KEYPAD:
            pos = next_pos
    return pos


with open(INPUT_FILE_NAME, "r") as input_file:
    instructions = [line.strip() for line in input_file]

pos = 1 + 1j
solution = ""
for instruction in instructions:
    pos = follow(instruction, pos)
    solution += str(KEYPAD[pos])

print(solution)
