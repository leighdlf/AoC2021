with open("data/02.txt", "r") as file:
    instructions = [line.strip("\n").split(" ") for line in file]


def final_position():
    depth, horizontal_position = 0, 0
    for instruction in instructions:
        if instruction[0] == "down":
            depth += int(instruction[1])
        elif instruction[0] == "up":
            depth -= int(instruction[1])
        elif instruction[0] == "forward":
            horizontal_position += int(instruction[1])
    return depth * horizontal_position


print(final_position())


def final_position2():
    depth, horizontal_position, aim = 0, 0, 0
    for instruction in instructions:
        if instruction[0] == "down":
            aim += int(instruction[1])
        elif instruction[0] == "up":
            aim -= int(instruction[1])
        elif instruction[0] == "forward":
            horizontal_position += int(instruction[1])
            depth += aim * int(instruction[1])
    return depth * horizontal_position


final_position2()

import lambdacalculus as lc
import sys

sys.setrecursionlimit(1_000_000)  # Won't work without.


def final_position_lc():
    horizontal_position = lc.zero
    depth = lc.zero
    for instruction in instructions:
        direction = instruction[0]
        delta_p = lc.int_to_church(int(instruction[1]))
        if direction == "down":
            depth = lc.add(depth)(delta_p)
        elif direction == "up":
            depth = lc.sub(depth)(delta_p)
        elif direction == "forward":
            horizontal_position = lc.add(horizontal_position)(delta_p)
    return lc.mul(depth)(horizontal_position)


def final_position_lc2():
    horizontal_position = lc.zero
    depth = lc.zero
    aim = lc.zero
    for instruction in instructions:
        direction = instruction[0]
        delta_p = lc.int_to_church(int(instruction[1]))
        if direction == "down":
            aim = lc.add(aim)(delta_p)
        elif direction == "up":
            aim = lc.sub(aim)(delta_p)
        elif direction == "forward":
            horizontal_position = lc.add(horizontal_position)(delta_p)
            depth = lc.add(depth)(lc.mul(aim)(delta_p))
    return lc.mul(depth)(horizontal_position)  # Slow.
