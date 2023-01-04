#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

program = []
with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        parts = line.strip().split(" ")
        command = [
            int(part) if part.lstrip("-").isnumeric() else part for part in parts
        ]

        program.append(command)

reg = {"a": 0, "b": 0, "c": 0, "d": 0}
pos = 0
while 0 <= pos < len(program):
    cmd = program[pos]
    # print(f"pos: {pos:2d} reg: {str(reg):45s} cmd: {str(cmd):20s}", end="")
    if cmd[0] == "cpy":
        value = cmd[1] if isinstance(cmd[1], int) else reg[cmd[1]]
        reg[cmd[2]] = value
        pos += 1
    elif cmd[0] == "inc":
        reg[cmd[1]] += 1
        pos += 1
    elif cmd[0] == "dec":
        reg[cmd[1]] -= 1
        pos += 1
    elif cmd[0] == "jnz":
        value = cmd[1] if isinstance(cmd[1], int) else reg[cmd[1]]
        if value != 0:
            pos += cmd[2]
        else:
            pos += 1
    # print(f" => pos: {pos:2d} reg: {str(reg):45s}")

print(reg["a"])
