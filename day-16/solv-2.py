#!/usr/bin/env python3

from collections import deque

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input-2"


def get_filler_data(start_state: str, disk_size: int) -> str:
    state = deque(start_state)
    print("data size:", len(state))
    while len(state) < disk_size:
        start_len = len(state)
        state = [*state, "0", *reversed(state)]
        for i in range(start_len + 1, len(state)):
            a_char = state[i]
            state[i] = "0" if a_char == "1" else "1"
        print("data size:", len(state))
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

print("disk size:", disk_size)
data = get_filler_data(start_state, disk_size)
print("got data")
# print(data)
checksum = get_checksum(data)
print(checksum)
