#!/usr/bin/env python3

from typing import Optional

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"


class Elf:
    def __init__(self, number: int, next_elf: Optional["Elf"] = None) -> None:
        self.number: int = number
        self.next: Optional["Elf"] = next_elf


def solve(elf_count: int) -> None:
    first = Elf(1)
    first.next = first
    prev = first
    for number in range(2, elf_count + 1):
        elf = Elf(number, first)
        prev.next = elf
        prev = elf
    current = first
    while current.next != current:
        current.next = current.next.next
        current = current.next
    print(current.number)


with open(INPUT_FILE_NAME, "r") as input_file:
    solve(int(input_file.read().strip()))
