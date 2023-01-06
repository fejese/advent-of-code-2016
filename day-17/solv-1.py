#!/usr/bin/env python3

from collections import deque
from hashlib import md5
from typing import Dict


# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

START: complex = 0j
TARGET: complex = 3 + 3j


DOOR_ORDER: str = list("UDLR")
OPEN_STATES: str = "bcdef"
DOOR_TO_MOVE: Dict[str, complex] = dict(zip(DOOR_ORDER, [-1j, 1j, -1 + 0j, 1 + 0j]))


def get_door_states(passcode: str, path: str) -> Dict[str, bool]:
    hash_base = passcode + path
    hash_digest = md5(hash_base.encode()).hexdigest()
    states = dict(zip(DOOR_ORDER, [ch in OPEN_STATES for ch in hash_digest[:4]]))
    # print("hash base:", hash_base, ", digest:", hash_digest, ", states:", states)
    return states


def solve(passcode: str) -> None:
    to_visit = deque([(START, "")])
    while to_visit:
        pos, path = to_visit.popleft()
        door_states = get_door_states(passcode, path)
        for door, is_open in door_states.items():
            if not is_open:
                continue
            new_pos = pos + DOOR_TO_MOVE[door]
            if not (START.imag <= new_pos.imag <= TARGET.imag):
                continue
            if not (START.real <= new_pos.real <= TARGET.real):
                continue
            new_path = path + door
            if new_pos == TARGET:
                print("solution: ", new_path)
                return
            to_visit.append((new_pos, new_path))

    print("there are no solutions")


with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        solve(line.strip())
