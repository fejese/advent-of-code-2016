#!/usr/bin/env python3

from collections import deque

# TEST: bool = True
TEST: bool = False

INPUT_FILE_NAME: str = "test-input" if TEST else "input"
SCREEN_WIDTH: int = 7 if TEST else 50
SCREEN_HEIGHT: int = 3 if TEST else 6


def process(grid, line):
    parts = line.split(" ")
    if parts[0] == "rect":
        w, h = [int(x) for x in parts[1].split("x")]
        for y in range(h):
            for _ in range(w):
                grid[y].popleft()
            for _ in range(w):
                grid[y].appendleft(1)
        return

    if parts[0] != "rotate":
        raise Exception(f"what: {parts}")

    if parts[1] == "column":
        x = int(parts[2].split("=")[1])
        by = int(parts[4])
        column = deque([grid[y][x] for y in range(SCREEN_HEIGHT)])
        column.rotate(by)
        for y in range(SCREEN_HEIGHT):
            grid[y][x] = column[y]
        return

    if parts[1] == "row":
        y = int(parts[2].split("=")[1])
        by = int(parts[4])
        grid[y].rotate(by)
        return

    raise Exception(f"what: {parts}")


def print_grid(grid, blank="."):
    for line in grid:
        for ch in line:
            print("#" if ch == 1 else blank, end="")
        print()
    print()


grid = [deque([0] * SCREEN_WIDTH) for _ in range(SCREEN_HEIGHT)]
with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        process(grid, line)
        # print_grid(grid)

print_grid(grid, blank=" ")
