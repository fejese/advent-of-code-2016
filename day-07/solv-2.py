#!/usr/bin/env python3

from collections import deque

# INPUT_FILE_NAME: str = "test-input-2"
INPUT_FILE_NAME: str = "input"


def is_aba(cache: deque, ch: str) -> bool:
    if len(cache) < 2:
        return False
    if cache[0] != ch:
        return False
    if cache[0] == cache[1]:
        return False
    return True


def does_support(line: str) -> int:
    # print(f"processing {line}")
    cache = deque(maxlen=2)
    in_subnet = False
    abas = set()
    babs = set()
    for ch in line:
        if ch in "[]":
            in_subnet = not in_subnet
            cache = deque(maxlen=2)
            continue

        if in_subnet:
            if is_aba(cache, ch):
                babs.add((cache[1], ch))
        elif is_aba(cache, ch):
            abas.add((ch, cache[1]))

        cache.append(ch)

    # print(f"  abas: {abas}")
    # print(f"  babs: {babs}")
    # print(f"  intersection: {abas.intersection(babs)}")

    return 1 if abas.intersection(babs) else 0


with open(INPUT_FILE_NAME, "r") as input_file:
    supports = sum(does_support(line.strip()) for line in input_file)

print(supports)
