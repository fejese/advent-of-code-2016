#!/usr/bin/env python3

import re

from collections import defaultdict, deque
from typing import Dict


# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"


NUMS: re.Pattern = re.compile(r"\b\d+\b")
TARGETS: re.Pattern = re.compile(r"\b(bot|output)\b")


class Bot:
    def __init__(
        self,
        bot_id: int,
        low_target: int,
        low_target_is_output: bool,
        high_target: int,
        high_target_is_output: bool,
    ) -> None:
        self.id = bot_id
        self.low_target = low_target
        self.low_target_is_output = low_target_is_output
        self.high_target = high_target
        self.high_target_is_output = high_target_is_output
        self.values = []

    @property
    def low(self) -> int:
        return min(self.values)

    @property
    def high(self) -> int:
        return max(self.values)

    def __repr__(self) -> str:
        low_target = f"{'O' if self.low_target_is_output else 'B'}-{self.low_target}"
        high_target = f"{'O' if self.high_target_is_output else 'B'}-{self.high_target}"
        return f"[#{self.id}: {self.values} -> {low_target}, {high_target}]"

    def process(
        self,
        bots: Dict[int, "Bot"],
        outputs: Dict[int, int],
        inputs: Dict[int, deque],
    ) -> None:
        if len(self.values) < 2:
            return

        target_is_output = [self.low_target_is_output, self.high_target_is_output]
        target = [self.low_target, self.high_target]
        value = [self.low, self.high]

        self.values = []

        for i in range(2):
            if target_is_output[i]:
                outputs[target[i]] = value[i]
            else:
                if target[i] in bots:
                    bots[target[i]].values.append(value[i])
                    bots[target[i]].process(bots, outputs, inputs)
                else:
                    inputs[target[i]].append(value[i])


bots: Dict[int, Bot] = {}
outputs: Dict[int, int] = {}
inputs: Dict[int, int] = defaultdict(deque)
with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        print(f"Line: {line.strip()}")
        if line.startswith("value"):
            value, bot_id = [int(x) for x in NUMS.findall(line)]
            if bot_id in bots:
                bots[bot_id].values.append(value)
                bots[bot_id].process(bots, outputs, inputs)
            else:
                inputs[bot_id].append(value)
        else:
            target_types = TARGETS.findall(line)[1:]
            bot_id, low_target, high_target = [int(x) for x in NUMS.findall(line)]
            bots[bot_id] = Bot(
                bot_id,
                low_target,
                target_types[0] == "output",
                high_target,
                target_types[1] == "output",
            )
            while inputs[bot_id]:
                bots[bot_id].values.append(inputs[bot_id].popleft())
                bots[bot_id].process(bots, outputs, inputs)
            if bot_id in inputs:
                del inputs[bot_id]

print(outputs[0] * outputs[1] * outputs[2])
