#!/usr/bin/env python3

import re

from collections import deque
from hashlib import md5

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

with open(INPUT_FILE_NAME, "r") as input_file:
    salt = input_file.read().strip()


index = 0
triplets = deque(maxlen=1001)
key_indexes = set()
limit = 1001
while index < limit:
    hash_digest = f"{salt}{index}"
    for _ in range(2017):
        hash_digest = md5(hash_digest.encode()).hexdigest()

    tmatch = re.findall(r"((.)\2{2})", hash_digest)
    if tmatch:
        triplets.append(tmatch[0][1])
        # print(f"found triplet: {index} => {hash_digest} => {tmatch[0][1]}")

        qmatch = re.findall(r"((.)\2{4})", hash_digest)
        if qmatch:
            quintuplets = set(m[1] for m in qmatch)
            print(f"found quintuplets: {index} => {quintuplets}")
            for idx, triplet_letter in enumerate(triplets, start=max(0, index - 1000)):
                if idx == index:
                    continue
                if triplet_letter in quintuplets:
                    print(
                        f"found key: {idx} => {triplet_letter}, {index} => {hash_digest} => {quintuplets}"
                    )
                    key_indexes.add(idx)
    else:
        triplets.append(None)

    index += 1
    if len(key_indexes) < 64:
        limit = index + 1002

# print(key_indexes)
print(sorted(key_indexes)[63])
