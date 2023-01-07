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

reg = {"a": 7, "b": 0, "c": 0, "d": 0}
pos = 0
while 0 <= pos < len(program):
    cmd = program[pos]
    # print(f"pos: {pos:2d} reg: {str(reg):45s} cmd: {str(cmd):20s}", end="")
    if cmd[0] == "cpy":
        if cmd[2] in reg:
            value = cmd[1] if isinstance(cmd[1], int) else reg[cmd[1]]
            reg[cmd[2]] = value
        pos += 1
    elif cmd[0] == "inc":
        if cmd[1] in reg:
            reg[cmd[1]] += 1
        pos += 1
    elif cmd[0] == "dec":
        if cmd[1] in reg:
            reg[cmd[1]] -= 1
        pos += 1
    elif cmd[0] == "jnz":
        value = cmd[1] if isinstance(cmd[1], int) else reg[cmd[1]]
        if value != 0:
            d = cmd[2] if isinstance(cmd[2], int) else reg[cmd[2]]
            pos += d
        else:
            pos += 1
    elif cmd[0] == "tgl":
        value = cmd[1] if isinstance(cmd[1], int) else reg[cmd[1]]
        target_pos = pos + reg[cmd[1]]
        if 0 <= target_pos < len(program):
            if len(program[target_pos]) == 2:
                if program[target_pos][0] == "inc":
                    program[target_pos][0] = "dec"
                else:
                    program[target_pos][0] = "inc"
            else:
                if program[target_pos][0] == "jnz":
                    program[target_pos][0] = "cpy"
                else:
                    program[target_pos][0] = "jnz"

        pos += 1

    # print(f" => pos: {pos:2d} reg: {str(reg):45s}")


print("registers:", reg)
print("solution:", reg["a"])
