#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

# x = 0 1 2 3 4
# y=0     1
# y=1   2 3 4
# y=2 5 6 7 8 9
# y=3   A B C
# y=4     D
KEYPAD = {}
KEYPAD.update({2 + 0j: 1})
KEYPAD.update({x + 1j: x + 1 for x in range(1, 4)})
KEYPAD.update({x + 2j: x + 5 for x in range(5)})
KEYPAD.update({x + 3j: f"{(x + 9):x}".upper() for x in range(1, 4)})
KEYPAD.update({2 + 4j: "D"})
print(KEYPAD)


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

pos = 2j
solution = ""
for instruction in instructions:
    pos = follow(instruction, pos)
    solution += str(KEYPAD[pos])

print(solution)
