#!/usr/bin/env python3

import re

from collections import deque
from dataclasses import dataclass
from typing import Dict, List, Optional, Set, Tuple

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"


START: complex = 0j
LINE_PATTERN: re.Pattern = re.compile(r".*x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T.*")


State = Tuple[complex, complex]


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


def get_neighbours(
    empty_space: complex, max_coord: complex, immovables: Set[complex]
) -> List[complex]:
    maybe_neighbours = set(
        empty_space + dx + 1j * dy
        for dx in (-1, 0, 1)
        for dy in (-1, 0, 1)
        if 0 <= empty_space.real + dx <= max_coord.real
        and 0 <= empty_space.imag + dy <= max_coord.imag
        and (dx == 0) != (dy == 0)
    )
    return maybe_neighbours.difference(immovables)


def solve(nodes: List[Node]) -> Optional[int]:
    movable_capacity: int = 0
    empty_space: complex = 0j

    for node in nodes:
        if node.used == 0:
            movable_capacity = node.size
            empty_space = node.coord
            break

    immovables: Set[complex] = set()
    max_coord: complex = 0j
    for node in nodes:
        if node.used > movable_capacity:
            immovables.add(node.coord)
        max_coord = max(max_coord.real, node.coord.real) + 1j * max(
            max_coord.imag, node.coord.imag
        )

    goal = max_coord.real + 0j

    state = (goal, empty_space)
    to_visit: deque = deque([state])
    visited: Dict[State, int] = {state: 0}

    while to_visit:
        state = to_visit.popleft()
        goal, empty_space = state
        steps = visited[state]
        new_steps = steps + 1
        empty_neighbours = get_neighbours(empty_space, max_coord, immovables)
        for empty_neighbour in empty_neighbours:
            if empty_neighbour == goal:
                if empty_space == 0j:
                    print("Finished!")
                    return new_steps
                new_state = (empty_space, goal)
            else:
                new_state = (goal, empty_neighbour)

            if new_state not in visited:
                visited[new_state] = new_steps
                to_visit.append(new_state)

    print("Finished search without finding solution")


with open(INPUT_FILE_NAME, "r") as input_file:
    nodes: List[Node] = [
        Node.from_line(line) for line in input_file if line.startswith("/")
    ]


print("solution:", solve(nodes))
