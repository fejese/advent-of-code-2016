#!/usr/bin/env python3

from collections import defaultdict, deque
from itertools import permutations
from typing import Dict, List, Set


# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"


Grid = Dict[complex, int]
EMPTY = -1
WALL = -2


def get_neighbours(grid: Grid, pos: complex) -> List[complex]:
    return [
        pos + dx + 1j * dy
        for dx in (-1, 0, 1)
        for dy in (-1, 0, 1)
        if (dx == 0) != (dy == 0)
        and (pos + dx + 1j * dy) in grid
        and grid[pos + dx + 1j * dy] != WALL
    ]


def get_distances(
    grid: Grid, source: complex, targets: Set[complex]
) -> Dict[complex, int]:
    visited: Set[complex] = {source}
    to_visit: Set[complex] = {source}
    distances: Dict[complex, int] = {source: 0}
    step = 1
    while to_visit and len(distances) < len(targets):
        new_to_visit: Set[complex] = set()
        for pos in to_visit:
            neighs = get_neighbours(grid, pos)
            for neigh in neighs:
                if neigh in visited:
                    continue
                visited.add(neigh)
                if neigh in targets:
                    distances[neigh] = step
                new_to_visit.add(neigh)

        to_visit = new_to_visit
        step += 1
    return distances


def solve(grid: Grid, start: complex, targets: List[complex]) -> int:
    pois = [start, *targets]
    distances: Dict[complex, Dict[complex, int]] = {
        poi: get_distances(grid, poi, set(pois)) for poi in pois
    }
    full_distances: Dict[str, int] = {}
    for order in permutations(targets):
        full_distance = 0
        prev = start
        for target in order:
            full_distance += distances[prev][target]
            prev = target
        full_distance += distances[prev][start]
        full_distances[str(order)] = full_distance

    # print("Potential solutions:")
    # for order, length in full_distances.items():
    #     print(f" - {order} => {length}")
    return min(full_distances.values())


grid: Grid = {}
start: complex
targets: List[complex] = []
with open(INPUT_FILE_NAME, "r") as input_file:
    for y, line in enumerate(input_file):
        for x, cell in enumerate(line.strip()):
            coord = x + 1j * y
            grid[coord] = cell
            if cell.isnumeric():
                num = int(cell)
                if num == 0:
                    start = coord
                else:
                    targets.append(coord)
                grid[coord] = num
            elif cell == "#":
                grid[coord] = WALL
            else:
                grid[coord] = EMPTY

print("solution:", solve(grid, start, targets))
