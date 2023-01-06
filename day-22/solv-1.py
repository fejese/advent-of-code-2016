#!/usr/bin/env python3

import re

from dataclasses import dataclass
from typing import List

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

LINE_PATTERN: re.Pattern = re.compile(r".*x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T.*")


@dataclass
class Node:
    coord: complex
    size: int
    used: int

    @property
    def avail(self) -> int:
        return self.size - self.used

    @classmethod
    def from_line(cls, line: str) -> "Node":
        match = LINE_PATTERN.match(line)
        if not match:
            raise Exception(f"wat: {line}")

        x, y, size, used, avail = [int(x) for x in match.groups()]
        if size != used + avail:
            raise Exception(f"wat2: {line}")

        return cls(x + 1j * y, size, used)


def solve(nodes: List[Node]) -> int:
    by_used = sorted(nodes, key=lambda n: n.used)
    by_avail = sorted(nodes, key=lambda n: n.avail)
    by_used_idx = 0
    by_avail_idx = 0
    count = 0

    while by_avail_idx < len(nodes) and 0 >= by_used[by_used_idx].used:
        by_used_idx += 1

    while (
        by_avail_idx < len(nodes)
        and by_avail[by_avail_idx].avail < by_used[by_used_idx].used
    ):
        by_avail_idx += 1
        while (
            by_avail_idx < len(nodes)
            and by_used_idx < len(nodes)
            and by_avail[by_avail_idx].avail >= by_used[by_used_idx].used
        ):
            by_used_idx += 1
            count += 1

    return count


with open(INPUT_FILE_NAME, "r") as input_file:
    nodes: List[Node] = [
        Node.from_line(line) for line in input_file if line.startswith("/")
    ]

print("solution:", solve(nodes))
