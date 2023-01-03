#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"


def process(line: str) -> int:
    # print(f"processing {line}")
    i = 0
    uncompressed_length = 0

    while i < len(line):
        if line[i] == "(":
            # print(f"  marker at {i}")
            marker_len = 0
            i += 1
            while line[i] != "x":
                marker_len = marker_len * 10 + int(line[i])
                i += 1
            # print(f"    marker_len: {marker_len}, i={i}")
            i += 1
            marker_count = 0
            while line[i] != ")":
                marker_count = marker_count * 10 + int(line[i])
                i += 1
            # print(f"    marker_count: {marker_count}, i={i}")
            i += marker_len + 1
            uncompressed_length += marker_count * marker_len
        else:
            # print(f"  normal: {i} => {line[i]}")
            uncompressed_length += 1
            i += 1

    return uncompressed_length


with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        print(process(line.strip()))
