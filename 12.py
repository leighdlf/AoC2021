def main(part):
    def construct_nodes():
        """Constructs nodes, returns a dictionary with the node as the key and links as a list."""
        with open("12.txt") as file:
            data = [tuple(line.strip().split('-')) for line in file.readlines()]

        caves_dict = {}
        for node in data:
            if node[0] not in caves_dict:
                caves_dict[node[0]] = [node[1]]
            else:
                caves_dict[node[0]].append(node[1])

            if node[1] not in caves_dict:
                caves_dict[node[1]] = [node[0]]
            else:
                caves_dict[node[1]].append(node[0])

        return caves_dict

    def find_cave_paths():
        """Uses depth first search to recursively find all paths from start to end"""
        caves = construct_nodes()
        paths = 0

        def find_path(current_cave, path, visited, vis_twice):
            """Recursive depth first path finding algorithm."""
            if current_cave.islower():  # Upper case/large caves can be visited multiple times.
                visited.add(current_cave)

            # Handles part 2;
            # one lower case cave can be visited twice in a path.
            next_vis = vis_twice
            if current_cave.islower():
                if current_cave in path:
                    if vis_twice:
                        next_vis = False
                    else:
                        return

            path.append(current_cave)

            if current_cave == 'end':
                nonlocal paths
                paths += 1
                visited.remove(current_cave)
                path.pop()  # Remove from path so all ends can be found.
                return

            else:
                for adj_caves in [cave for cave in caves[current_cave]]:

                    if adj_caves not in visited:
                        find_path(adj_caves, path, visited, next_vis)

                    elif vis_twice and adj_caves != 'start':
                        find_path(adj_caves, path, visited, next_vis)

                if current_cave in visited:
                    visited.remove(current_cave)

                path.pop()  # Remove from path/visited as it can be in multiple paths.

        find_path(current_cave='start', path=[], visited=set(), vis_twice=True if part == 2 else False)

        return paths

    if part == 1:
        print(f'For part 1 there where {find_cave_paths()} possible paths through the cave network.')
    if part == 2:
        print(f'For part 2 there where {find_cave_paths()} possible paths through the cave network.')


if __name__ == "__main__":
    main(1)
    main(2)
