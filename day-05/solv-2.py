#!/usr/bin/env python3

from hashlib import md5

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

PLACEHOLDER: str = "_"

with open(INPUT_FILE_NAME, "r") as input_file:
    door_id = input_file.read().strip()

i = 0
password = [PLACEHOLDER] * 8
while PLACEHOLDER in password:
    while True:
        hash_digest = md5((f"{door_id}{i}").encode()).hexdigest()
        i += 1
        if hash_digest.startswith("00000"):
            pass_ch_pos = int(hash_digest[5], 16)
            pass_ch = hash_digest[6]
            if pass_ch_pos >= 8:
                print(
                    "Skipping as position is invalid:",
                    i - 1,
                    hash_digest,
                    pass_ch_pos,
                    pass_ch,
                    "".join(password),
                )
                continue
            if password[pass_ch_pos] != PLACEHOLDER:
                print(
                    "Skipping as position is already filled:",
                    i - 1,
                    hash_digest,
                    pass_ch_pos,
                    pass_ch,
                    "".join(password),
                )
                continue
            password[pass_ch_pos] = pass_ch
            print("Found:", i - 1, hash_digest, pass_ch_pos, pass_ch, "".join(password))
            break

print("".join(password))
