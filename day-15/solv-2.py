#!/usr/bin/env python3

from dataclasses import dataclass
from re import findall
from typing import List

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input-2"


@dataclass
class Disc:
    num: int
    positions: int
    starting_position: int


discs: List[Disc] = []
with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        nums = [int(x) for x in findall(r"\b\d+\b", line)]
        discs.append(Disc(nums[0], nums[1], nums[3]))

start_time = 0
found = False
while not found:
    found = True
    for disc in discs:
        if (start_time + disc.num + disc.starting_position) % disc.positions != 0:
            found = False
            break
    if not found:
        start_time += 1

print(start_time)
