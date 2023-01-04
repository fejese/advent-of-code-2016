#!/usr/bin/env python3

from collections import deque

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"


def get_filler_data(start_state: str, disk_size: int) -> str:
    state = deque(start_state)
    # print("".join(state))
    while len(state) < disk_size:
        start_len = len(state)
        state.append("0")
        for i in range(start_len - 1, -1, -1):
            a_char = state[i]
            state.append("0" if a_char == "1" else "1")
        # print("".join(state))

    return "".join(state)[:disk_size]


def get_checksum(data: str) -> str:
    checksum = data
    while len(checksum) % 2 == 0:
        new_checksum = ""
        for pos in range(0, len(checksum), 2):
            new_checksum += "1" if checksum[pos] == checksum[pos + 1] else "0"
        checksum = new_checksum
    return checksum


with open(INPUT_FILE_NAME, "r") as input_file:
    start_state = input_file.readline().strip()
    disk_size = int(input_file.readline().strip())

data = get_filler_data(start_state, disk_size)
# print(data)
checksum = get_checksum(data)
print(checksum)
