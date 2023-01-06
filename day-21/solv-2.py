#!/usr/bin/env python3

from itertools import permutations
from typing import List, Tuple

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input-2"


def solve(password: Tuple[str], instructions: List[str]) -> str:
    scrambled = list(password)
    # print("start: ", scrambled)
    for instruction in instructions:
        parts = instruction.split(" ")
        if parts[0] == "swap":
            if parts[1] == "position":
                pos_a = int(parts[2])
                pos_b = int(parts[5])
            elif parts[1] == "letter":
                pos_a = scrambled.index(parts[2])
                pos_b = scrambled.index(parts[5])
            else:
                raise Exception(f"wat: {parts}")
            tmp = scrambled[pos_a]
            scrambled[pos_a] = scrambled[pos_b]
            scrambled[pos_b] = tmp
        elif parts[0] == "rotate":
            if parts[3].startswith("step"):
                amount = int(parts[2])
                if parts[1] == "right":
                    amount *= -1
            elif parts[1] == "based":
                pos_a = scrambled.index(parts[6])
                amount = -1 - pos_a
                if pos_a >= 4:
                    amount -= 1
            else:
                raise Exception(f"wat: {parts}")

            while amount < -len(scrambled):
                amount += len(scrambled)
            while amount > len(scrambled):
                amount -= len(scrambled)

            scrambled = scrambled[amount:] + scrambled[:amount]
        elif parts[0] == "reverse":
            pos_a = int(parts[2])
            pos_b = int(parts[4])
            scrambled = (
                scrambled[:pos_a]
                + list(reversed(scrambled[pos_a : pos_b + 1]))
                + scrambled[pos_b + 1 :]
            )
        elif parts[0] == "move":
            pos_a = int(parts[2])
            pos_b = int(parts[5])
            if pos_a < pos_b:
                scrambled = (
                    scrambled[:pos_a]
                    + scrambled[pos_a + 1 : pos_b + 1]
                    + [scrambled[pos_a]]
                    + scrambled[pos_b + 1 :]
                )
            elif pos_a > pos_b:
                scrambled = (
                    scrambled[:pos_b]
                    + [scrambled[pos_a]]
                    + scrambled[pos_b:pos_a]
                    + scrambled[pos_a + 1 :]
                )
        else:
            raise Exception(f"wat: {parts}")

        # print(instruction, "=>", scrambled)

    # print("".join(scrambled))
    return "".join(scrambled)


with open(INPUT_FILE_NAME, "r") as input_file:
    scrambled = input_file.readline().strip()
    instructions = [line.strip() for line in input_file]

for password in sorted(permutations(scrambled)):
    scrambled_i = solve(password, instructions)
    print("".join(password), "=>", scrambled_i)
    if scrambled == scrambled_i:
        print("^^^^^ found!")
        break
