#!/usr/bin/env python3

from collections import deque

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"


def is_abba(cache: deque, ch: str) -> bool:
    if len(cache) < 3:
        return False
    if cache[0] != ch:
        return False
    if cache[1] != cache[2]:
        return False
    if cache[0] == cache[1]:
        return False
    return True


def does_support(line: str) -> int:
    cache = deque(maxlen=3)
    in_subnet = False
    found_outside = False
    for ch in line:
        if ch in "[]":
            in_subnet = not in_subnet
            cache = deque(maxlen=3)
            continue

        if in_subnet:
            if is_abba(cache, ch):
                return 0
        elif not found_outside and is_abba(cache, ch):
            found_outside = True

        cache.append(ch)
    return 1 if found_outside else 0


with open(INPUT_FILE_NAME, "r") as input_file:
    supports = sum(does_support(line.strip()) for line in input_file)

print(supports)
