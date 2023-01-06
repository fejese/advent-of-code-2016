#!/usr/bin/env python3

from typing import Optional

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"


class Elf:
    def __init__(
        self,
        number: int,
        prev_elf: Optional["Elf"] = None,
        next_elf: Optional["Elf"] = None,
    ) -> None:
        self.number: int = number
        self.prev: Optional["Elf"] = prev_elf
        self.next: Optional["Elf"] = next_elf


def solve(elf_count: int) -> None:
    first = Elf(1)
    first.prev = first
    first.next = first
    prev = first
    for number in range(2, elf_count + 1):
        elf = Elf(number, prev, first)
        prev.next = elf
        first.prev = elf
        prev = elf

    elves_left = elf_count
    current = first
    to_eliminate = current
    for _ in range(elves_left // 2):
        to_eliminate = to_eliminate.next

    while elves_left > 1:
        to_eliminate.prev.next = to_eliminate.next
        to_eliminate.next.prev = to_eliminate.prev

        current = current.next
        to_eliminate = to_eliminate.next
        if elves_left % 2 == 1:
            to_eliminate = to_eliminate.next
        elves_left -= 1

    print(current.number)


with open(INPUT_FILE_NAME, "r") as input_file:
    solve(int(input_file.read().strip()))
