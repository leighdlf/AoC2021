import numpy as np


def main(part):
    with open("data/05.txt") as file:
        line_segments = \
            [
                [[int(n) for n in line.split(',')] for line in lines.strip().split('->')]
                for lines in file.readlines()
            ]
        line_segments.sort()  # Sort to aid in generating the array.
        # Generate a x-max * y-max array. Inefficient generation.
        diagram = np.array(
            [
                [0 for x in range(max([x[0][0] for x in line_segments] + [x[1][0] for x in line_segments]) + 1)]
                for y in range(max([x[0][1] for x in line_segments] + [x[1][1] for x in line_segments]) + 1)
            ])
        # Exclude diagonal lines.
        h_v_lines = \
            [
                xy for xy in line_segments if xy[0][0] == xy[1][0] or xy[0][1] == xy[1][1]
            ]

    # Marking the points for horizontal lines.
    x_lines = [xy for xy in h_v_lines if xy[0][1] == xy[1][1]]
    for line in x_lines:
        (start_end) = line[0][0], line[1][0]
        for x_point in range(min(start_end), max(start_end) + 1):
            diagram[line[0][1]][x_point] += 1  # y-row then x-column.

    # Marking the points for vertical lines.
    y_lines = [xy for xy in h_v_lines if xy[0][0] == xy[1][0]]
    for line in y_lines:
        (start_end) = line[0][1], line[1][1]
        for y_point in range(min(start_end), max(start_end) + 1):
            diagram[y_point][line[0][0]] += 1

    # Marking the points for diagonal lines.
    if part == 2:
        d_lines = [xy for xy in line_segments if xy not in h_v_lines]
        for line in d_lines:
            i_x = (1 if line[0][0] < line[1][0] else -1)  # Determines the direction of the line
            x_points = [p for p in range(line[0][0], line[1][0] + i_x, i_x)]

            i_y = (1 if line[0][1] < line[1][1] else -1)
            y_points = [p for p in range(line[0][1], line[1][1] + i_y, i_y)]

            for d_point in range(len(x_points)):  # length of x is the same as y.
                diagram[y_points[d_point]][x_points[d_point]] += 1

    # Counting how many times the lines overcrowds each other.
    diagram_overlap_count = 0
    for row in diagram:
        for point in row:
            if point > 1:
                diagram_overlap_count += 1
    print(diagram_overlap_count)


if __name__ == "__main__":
    main(1)
    main(2)
