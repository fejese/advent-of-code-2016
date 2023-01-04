#!/usr/bin/env python3

from collections import deque
from typing import List, Tuple

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

Grid = List[List[int]]
C = Tuple[int, int]

UNKNOWN: int = -2
WALL: int = -1


def init_grid(grid: Grid, magic_number: int) -> None:
    for y in range(len(grid)):
        row = grid[y]
        for x in range(len(row)):
            formula = x * x + 3 * x + 2 * x * y + y + y * y + magic_number
            bits = 0
            mask = 1
            while formula:
                # print(f"formula: {formula} mask: {mask} / {mask:b} bits: {bits}"
                if formula & mask:
                    bits += 1
                    formula -= mask
                mask <<= 1
            # print(f"formula: {formula} mask: {mask} / {mask:b} bits: {bits}"
            if bits % 2 == 1:
                row[x] = WALL


def print_grid(grid: Grid) -> None:
    for line in grid:
        for cell in line:
            if cell == WALL:
                print("[##]", end="")
            elif cell == UNKNOWN:
                print("[..]", end="")
            else:
                print(f"[{cell:2}]", end="")
        print()
    print()


def get_neighbours(cell: C) -> List[C]:
    return [
        (cell[0] + dx, cell[1] + dy)
        for dx in (-1, 0, 1)
        for dy in (-1, 0, 1)
        if ((dx == 0) != (dy == 0)) and (0 <= cell[0] + dx) and (0 <= cell[1] + dy)
    ]


def fill_grid(grid: Grid, start: C, limit: int) -> int:
    grid[start[1]][start[0]] = 0
    to_visit: deque = deque([start])
    limit_count = 1
    while to_visit:
        cell = to_visit.popleft()
        cell_value = grid[cell[1]][cell[0]]
        print(f"visiting {cell} ({cell_value})")
        if cell_value == limit:
            print(f"  skipping")
            continue
        neighs = get_neighbours(cell)
        print(f"  neighs: {neighs}")
        for neigh in get_neighbours(cell):
            neigh_value = grid[neigh[1]][neigh[0]]
            print(f"  checking {neigh} ({neigh_value})")
            if neigh_value == WALL:
                continue
            if 0 <= neigh_value <= cell_value + 1:
                continue
            if neigh_value == UNKNOWN:
                limit_count += 1
            grid[neigh[1]][neigh[0]] = cell_value + 1
            to_visit.append(neigh)
    return limit_count


with open(INPUT_FILE_NAME, "r") as input_file:
    magic_number = int(input_file.readline().strip())

grid: Grid = [[UNKNOWN] * 51 for _ in range(52)]
init_grid(grid, magic_number)
print_grid(grid)
result = fill_grid(grid, (1, 1), 50)
print_grid(grid)
print(result)
