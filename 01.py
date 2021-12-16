with open("data/01.txt", "r") as file:
    data = [int(n) for n in file]


def part_one():
    larger_count, i = 0, 0
    while i < len(data) - 1:  # Prevent indexing outside bounds.
        if data[i + 1] > data[i]:
            larger_count += 1
        i += 1
    print(larger_count)


part_one()


def part_two():
    larger_count, i = 0, 0
    while i < len(data) - 3:  # Prevent indexing outside bounds.
        if sum([data[i + 1], data[i + 2], data[i + 3]]) > sum([data[i], data[i + 1], data[i + 2]]):
            larger_count += 1
        i += 1
    print(larger_count)


part_two()
