import numpy as np


def main(part):
    with open("11.txt") as file:
        data = [[n for n in line.strip()] for line in file.readlines()]
    array = np.array(data, dtype=np.uint8)
    has_flashed = np.full_like(array, False, dtype=np.bool_)
    total_flashes = 0

    def get_adjacent_locations(row, column):
        """Returns the adjacent locations to a point on a grid,
        they are returned as a list of tuples in (row, column) form.
        """
        adjacent_locations = list(filter(lambda l: 0 <= l[0] < len(array[0])
                                         and 0 <= l[1] < len(array), [
                                             (row - 1, column - 1),
                                             (row - 1, column),
                                             (row - 1, column + 1),
                                             (row, column - 1),
                                             (row, column + 1),
                                             (row + 1, column - 1),
                                             (row + 1, column),
                                             (row + 1, column + 1),
                                         ]))
        return adjacent_locations

    def inc_by_uint(row, column):
        """Increments the octopuses energy level."""
        array[row, column] += np.uint8(1)

    def first_increase():
        """First part of a step, increase each ncrements the octopuses energy level."""
        for row in range(len(array[0])):
            for column in range(len(array)):
                inc_by_uint(row, column)

    def flash(row, column):
        """Flashes an octopus if its energy level is 9+,
        increments its neighbours energy levels by 1, then recursively flashes each neighbour.
        """
        if array[row][column] <= np.uint8(9) or has_flashed[row][column] == True:
            return
        else:
            has_flashed[row][column] = np.bool_(True)
            nonlocal total_flashes; total_flashes += 1
            for adjacent in get_adjacent_locations(row, column):
                inc_by_uint(adjacent[0], adjacent[1])
                flash(adjacent[0], adjacent[1])

    def reset_flashed():
        """If an octopus has flashed that step, it's energy level is reset to 0 at the end."""
        for row in range(len(array[0])):
            for column in range(len(array)):
                if array[row, column] > 9:
                    array[row, column] = np.uint8(0)

    def step():
        """Performs a step."""
        steps = 100 if part == 1 else 1000
        for step in range(steps):
            first_increase()
            for row in range(len(array[0])):
                for column in range(len(array)):
                    flash(row, column)

            nonlocal has_flashed
            if has_flashed.sum() == has_flashed.size:
                print(step + 1)  # +1 to account for starting step offset.
                break
            reset_flashed()

            has_flashed = np.full_like(array, False, dtype=np.bool_)

    step()
    if part == 1:
        print(total_flashes)


if __name__ == "__main__":
    main(1)
    main(2)
