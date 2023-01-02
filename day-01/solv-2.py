#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input-2"
INPUT_FILE_NAME: str = "input"


DS = [1j, 1, -1j, -1]


def solve(line: str) -> int:
    di = 0
    pos = 0j
    visited = set()
    visited.add(pos)
    for step in line.strip().split(", "):
        # print(pos)
        if step.startswith("L"):
            di = (di - 1) % 4
        else:
            di = (di + 1) % 4

        for _ in range(int(step[1:])):
            pos += DS[di]
            print(pos, visited)
            if pos in visited:
                print(pos, visited)
                return int(abs(pos.imag) + abs(pos.real))

            visited.add(pos)

    print(visited)
    return None


with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        print(solve(line))


# 163: low
