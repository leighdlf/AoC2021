def read_file(file_path: str) -> list[list[int]]:
    """Reads the input file and converts it into a list of ints, one list per line."""
    with open(file_path) as file:
        data = [[int(n) for n in line.strip()] for line in file.readlines()]

    return data


def extend_data(data: list[list[int]]) -> list[list[int]]:
    """Increases the cave size for part 2."""
    offset = len(data)

    # Extends the rows 5 times
    for row in data:
        for _ in range(offset * 4):  # 4 as 5* larger includes the original data.
            new_risk_level = row[-offset] + 1
            if new_risk_level > 9:
                new_risk_level = 1
            row.append(new_risk_level)

    # Extends downwards by adding new rows.
    for _ in range(offset * 4):
        new_row: list[int] = []
        for template_risk_level in data[-offset]:
            new_risk_level = template_risk_level + 1
            if new_risk_level > 9:
                new_risk_level = 1
            new_row.append(new_risk_level)
        data.append(new_row)

    return data


def get_adjacent_positions(row: int, column: int, row_length: int, col_length: int) -> list[tuple[int, int]]:
    """Returns the adjacent locations to a point on a grid,
    they are returned as a list of tuples in (row, column) form.
    """
    adjacent_locations = list(filter(
        lambda l: 0 <= l[0] < row_length and 0 <= l[1] < col_length, [
            (row - 1, column), (row, column - 1), (row, column + 1), (row + 1, column)
        ]))

    return adjacent_locations


def construct_graph(data: list[list[int]]) -> dict:
    """Constructs a list of nodes, with their edges connected, from the data."""
    graph_size = len(data)

    # Initialises a dict of nodes.
    nodes = {}
    for r_ind, row in enumerate(data):
        for c_ind, col in enumerate(row):
            # list: 0: risk, 1: previous, 2: local goal, 3: visited, 4: edges.
            nodes[(r_ind, c_ind)] = [col, None, float('inf'), False, []]
            nodes[(r_ind, c_ind)][4] = get_adjacent_positions(r_ind, c_ind, graph_size, graph_size)

    return nodes


def update_local_goal(graph: dict, current_node: tuple[int, int], pos_prev_node: tuple[int, int]) -> None:
    """Determines if this node is part of the shortest path."""
    #  If the risk from going from the previous node to this one is less than the current nodes local goal
    if graph[pos_prev_node][2] + graph[current_node][0] < graph[current_node][2]:
        graph[current_node][1] = pos_prev_node  # Mark as previous node
        #  Update the local goal to be the current risk plus the previous local goal.
        graph[current_node][2] = graph[pos_prev_node][2] + graph[current_node][0]


def find_lowest_risk_path(graph: dict, start: tuple[int, int], end: tuple[int, int]) -> int:
    """Finds the lowest risk score for traversing the cave, uses Dijkstra's algorithm."""
    nodes_to_visit: list[tuple[int, int]] = []
    graph[start][2] = 0
    nodes_to_visit.append(start)

    while nodes_to_visit:
        current_node = nodes_to_visit[0]
        if graph[current_node][3]:  # Has it been visited?
            nodes_to_visit.remove(current_node)
            continue
        for edge in graph[current_node][-1]:
            update_local_goal(graph, edge, current_node)
            graph[current_node][3] = True  # Mark as visited.
            nodes_to_visit.append(edge)
            if edge == end:
                nodes_to_visit.remove(edge)
        nodes_to_visit.remove(current_node)

        nodes_to_visit.sort(key=lambda n: graph[n][2])  # Could be optimised.

    return graph[end][2]


def main(part: int) -> None:
    data: list[list[int]] = read_file('data/15.txt')
    if part == 2:
        data = extend_data(data)
    graph: dict = construct_graph(data)

    print(f'For {"Part 1" if part == 1 else "Part 2"} '
          f'the total lowest risk is: {find_lowest_risk_path(graph, (0, 0), (len(data) - 1, len(data) - 1))}')


if __name__ == "__main__":
    main(1)
    main(2)
