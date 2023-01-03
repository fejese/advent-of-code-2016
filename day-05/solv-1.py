#!/usr/bin/env python3

from hashlib import md5

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

with open(INPUT_FILE_NAME, "r") as input_file:
    door_id = input_file.read().strip()

i = 0
password = ""
for _ in range(8):
    while True:
        hash_digest = md5((f"{door_id}{i}").encode()).hexdigest()
        i += 1
        if hash_digest.startswith("00000"):
            pass_ch = hash_digest[5]
            password += pass_ch
            print(i - 1, hash_digest, pass_ch, password)
            break

print(password)
