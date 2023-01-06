#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input-2"


TRAP: str = "^"
SAFE: str = "."


def solve(rows: int, first_line: str) -> None:
    safe_count = first_line.count(".")
    last_line = f".{first_line}."
    # print(first_line, safe_count)
    for line_no in range(1, rows):
        new_line = ""
        new_safe_count = 0
        for pos in range(1, len(last_line) - 1):
            if last_line[pos - 1] != last_line[pos + 1]:
                new_line += TRAP
            else:
                new_line += SAFE
                new_safe_count += 1
        # print(new_line, new_safe_count)
        last_line = f".{new_line}."
        safe_count += new_safe_count

    print(safe_count)
    print()


with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        parts = line.strip().split(" ")
        solve(int(parts[0]), parts[1])
