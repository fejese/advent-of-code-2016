#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

CH_COUNT = ord("z") - ord("a") + 1

with open(INPUT_FILE_NAME, "r") as input_file:
    lines = [line.strip() for line in input_file]


id_sum = 0
for line in lines:
    rest, checksum = line.strip().split("[")
    checksum = checksum.rstrip("]")
    name, sector_id = rest.rsplit("-", 1)
    sector_id = int(sector_id)
    counts = {}
    order_by_ch = {}
    for ch in name:
        if ch == "-":
            continue
        if ch not in counts:
            order_by_ch[ch] = len(counts)
            counts[ch] = 1
        else:
            counts[ch] += 1

    def sorting_score(item):
        return (item[1], CH_COUNT - ord(item[0]))

    ordered = sorted(counts.items(), key=sorting_score, reverse=True)
    actual_checksum = "".join([item[0] for item in ordered[:5]])
    if checksum == actual_checksum:
        id_sum += sector_id

print(id_sum)
