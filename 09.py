import numpy as np


def main():
    with open("09.txt") as file:
        data = [[n for n in line.strip()] for line in file.readlines()]

    array = np.array(data, dtype=np.int8)

    def get_adjacent(y, x):
        """Returns the adjacent values and coordinates in (col, row) as a tuple of lists."""
        adjacent_coordinates = list(filter(lambda n: n[0] is not None,
                                           [(y - 1, x) if y > 0 else (None, None),
                                            (y + 1, x) if y < len(array) - 1 else (None, None),
                                            (y, x - 1) if x > 0 else (None, None),
                                            (y, x + 1) if x < len(array[0]) - 1 else (None, None)]))
        adjacent_values = [array[ac[0]][ac[1]] for ac in adjacent_coordinates]
        return adjacent_values, adjacent_coordinates

    def get_low_points():
        """Returns the low points on the heightmap, as a tuple of values and coordinates."""
        low_point_values = []
        low_point_coordinates = []
        for x in range(len(array[0])):
            for y in range(len(array)):
                if array[y][x] < min(get_adjacent(y, x)[0]):
                    low_point_values.append(array[y][x] + 1)
                    low_point_coordinates.append((y, x))
        return low_point_values, low_point_coordinates

    low_points = get_low_points()

    def traverse_basin(low_point):
        """Traverses the heightmap from the low points, and finds basins that ar bound by height values of 9."""
        # Used a set as some points where counting more than once.
        mapped, not_mapped = {(low_point[0], low_point[1])}, []
        not_mapped += [point for point in get_adjacent(low_point[0], low_point[1])[1]
                       if array[point[0]][point[1]] != 9]
        while not_mapped:
            unmapped = not_mapped.pop()
            mapped.add(unmapped)
            neighbours = [point for point in get_adjacent(unmapped[0], unmapped[1])[1]
                          if array[point[0]][point[1]] != 9]
            for neighbour in neighbours:
                if neighbour not in mapped:  # TODO counting some more than once.
                    not_mapped.append(neighbour)
        return mapped

    def get_basins():
        """Using traverse_basin() returns a list of the basins"""
        basin_list = []
        for low_point in low_points[1]:
            basin_list.append(traverse_basin(low_point))
        return basin_list

    basins = get_basins()

    def three_largest_product():
        """ Returns the product of the area/size of the three largest basins."""
        area = [len(b) for b in basins]
        area.sort(reverse=True)
        return area[0] * area[1] * area[2]

    print(sum(low_points[0]))
    print(three_largest_product())


if __name__ == "__main__":
    main()
