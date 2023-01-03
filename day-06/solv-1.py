#!/usr/bin/env python3

from collections import defaultdict

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

freq = defaultdict(lambda: defaultdict(int))
with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        for idx, ch in enumerate(line.strip()):
            freq[idx][ch] += 1


password = ""
for idx in sorted(freq.keys()):
    idx_freq = freq[idx]
    ch = sorted(idx_freq.items(), key=lambda item: item[1], reverse=True)[0][0]
    password += ch

print(password)
