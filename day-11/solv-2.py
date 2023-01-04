#!/usr/bin/env python3

from collections import UserList, defaultdict
from copy import copy
from dataclasses import dataclass, replace
from re import findall
from typing import Dict, List, Tuple, TypeVar

# INPUT_FILE_NAME: str = "test-input-2"
INPUT_FILE_NAME: str = "input-2"


T = TypeVar("T")


@dataclass
class Pair:
    m: int
    g: int

    def __lt__(self, other: "Pair") -> bool:
        return (self.m, self.g) < (other.m, other.g)

    def __hash__(self) -> int:
        return (self.m, self.g).__hash__()

    def move_m(self, d: int) -> "Pair":
        return replace(self, m=self.m + d)

    def move_g(self, d: int) -> "Pair":
        return replace(self, g=self.g + d)


class Pairs(UserList, List[Pair]):
    def __hash__(self) -> int:
        return tuple(sorted(self)).__hash__()

    @property
    def solution(self) -> bool:
        return all(pair == Pair(4, 4) for pair in self)

    @property
    def valid(self) -> bool:
        generators_per_floor = defaultdict(set)
        microchips_per_floor = defaultdict(set)
        for idx, pair in enumerate(self):
            generators_per_floor[pair.g].add(idx)
            microchips_per_floor[pair.m].add(idx)

        for floor, idxs in microchips_per_floor.items():
            if not generators_per_floor[floor]:
                continue
            for idx in idxs:
                if not idx in generators_per_floor[floor]:
                    return False

        return True


Elevator = int
State = Tuple[Elevator, Pairs]


def solve(start_state: State) -> int:
    step = 0
    states = set([start_state])
    visited = set()
    while states:
        step += 1
        new_states = set()
        for state in states:
            visited.add(state)
            elevator, pairs = state
            generators_per_floor = defaultdict(set)
            microchips_per_floor = defaultdict(set)
            for idx, pair in enumerate(pairs):
                generators_per_floor[pair.g].add(idx)
                microchips_per_floor[pair.m].add(idx)

            ds = []
            if elevator < 4:
                ds.append(1)
            if elevator > 1:
                ds.append(-1)

            for d in ds:
                for moving_idx in microchips_per_floor[elevator]:
                    new_pairs = copy(pairs)
                    new_pairs[moving_idx] = new_pairs[moving_idx].move_m(d)

                    new_state = (elevator + d, new_pairs)
                    if new_state not in visited:
                        if new_pairs.solution:
                            return step
                        if new_pairs.valid:
                            new_states.add(new_state)

                    for other_moving_idx in microchips_per_floor[elevator]:
                        if moving_idx == other_moving_idx:
                            continue
                        new_pairs = copy(pairs)
                        new_pairs[moving_idx] = new_pairs[moving_idx].move_m(d)
                        new_pairs[other_moving_idx] = new_pairs[
                            other_moving_idx
                        ].move_m(d)

                        new_state = (elevator + d, new_pairs)
                        if new_state not in visited:
                            if new_pairs.solution:
                                return step
                            if new_pairs.valid:
                                new_states.add(new_state)

                    for other_moving_idx in generators_per_floor[elevator]:
                        new_pairs = copy(pairs)
                        new_pairs[moving_idx] = new_pairs[moving_idx].move_m(d)
                        new_pairs[other_moving_idx] = new_pairs[
                            other_moving_idx
                        ].move_g(d)

                        new_state = (elevator + d, new_pairs)
                        if new_state not in visited:
                            if new_pairs.solution:
                                return step
                            if new_pairs.valid:
                                new_states.add(new_state)

                for moving_idx in generators_per_floor[elevator]:
                    new_pairs = copy(pairs)
                    new_pairs[moving_idx] = new_pairs[moving_idx].move_g(d)

                    new_state = (elevator + d, new_pairs)
                    if new_state not in visited:
                        if new_pairs.solution:
                            return step
                        if new_pairs.valid:
                            new_states.add(new_state)

                    for other_moving_idx in generators_per_floor[elevator]:
                        if moving_idx == other_moving_idx:
                            continue
                        new_pairs = copy(pairs)
                        new_pairs[moving_idx] = new_pairs[moving_idx].move_g(d)
                        new_pairs[other_moving_idx] = new_pairs[
                            other_moving_idx
                        ].move_g(d)

                        new_state = (elevator + d, new_pairs)
                        if new_state not in visited:
                            if new_pairs.solution:
                                return step
                            if new_pairs.valid:
                                new_states.add(new_state)

        states = new_states
        print(step, len(states), len(visited))

    return step


generators: Dict[str, int] = {}
microchips: Dict[str, int] = {}
with open(INPUT_FILE_NAME, "r") as input_file:
    for floor, line in enumerate(input_file, start=1):
        microchips_on_this_floor = findall(r"\b\w+(?=-compatible microchip)", line)
        for microchip in microchips_on_this_floor:
            if microchip in microchips:
                raise Exception(f"duplicate microchip: {microchip}")
            microchips[microchip] = floor
        generators_on_this_floor = findall(r"\b\w+(?= generator)", line)
        for generator in generators_on_this_floor:
            if generator in generators:
                raise Exception(f"duplicate generator: {generator}")
            generators[generator] = floor


mismatched_names = set(generators.keys()).symmetric_difference(microchips.keys())
if mismatched_names:
    raise Exception(f"not all generators and microchips have pairs: {mismatched_names}")

pairs: Pairs = Pairs(
    [
        Pair(m=microchip_floor, g=generators[name])
        for name, microchip_floor in microchips.items()
    ]
)

print(solve(tuple([1, pairs])))
