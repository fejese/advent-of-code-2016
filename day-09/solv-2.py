#!/usr/bin/env python3

from typing import Tuple


# INPUT_FILE_NAME: str = "test-input-2"
INPUT_FILE_NAME: str = "input"


def resolve_marker(line: str, marker_start: int) -> Tuple[int, int]:
    total_uncompressed_length = 0
    i = marker_start
    if line[i] != "(":
        raise Exception(f"wat {i}, {line}")

    marker_len = 0
    i += 1
    while line[i] != "x":
        marker_len = marker_len * 10 + int(line[i])
        i += 1
    i += 1
    marker_count = 0
    while line[i] != ")":
        marker_count = marker_count * 10 + int(line[i])
        i += 1
    i += 1

    buffer_start = i

    while i < buffer_start + marker_len:
        if line[i] == "(":
            compressed_length, uncompressed_length = resolve_marker(line, i)
            total_uncompressed_length += marker_count * uncompressed_length
            i += compressed_length
        else:
            total_uncompressed_length += marker_count
            i += 1

    return i - marker_start, total_uncompressed_length


def process(line: str) -> int:
    # print(f"processing {line}")
    i = 0
    total_uncompressed_length = 0

    while i < len(line):
        if line[i] == "(":
            compressed_length, uncompressed_length = resolve_marker(line, i)
            i += compressed_length
            total_uncompressed_length += uncompressed_length
        else:
            total_uncompressed_length += 1
            i += 1

    return total_uncompressed_length


with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        print(process(line.strip()))
