import re
from operator import itemgetter

import numpy as np


def get_data(file_path: str) -> str:
    """Opens the file and returns its content as a string."""
    with open(file_path) as file:
        return file.read()


def get_template(data: str) -> list[str]:
    """Returns the polymer template as a list of strings/chars."""
    return list(re.findall('[A-Z]{3,}', data)[0])


def get_insertion_rules(data: str) -> dict[str: int]:
    """Returns a dictionary of the insertion rules.
    The pair is the key and the value is the polymer that should be inserted between.
    """
    return dict(zip(re.findall('([A-Z]{2})\\s->', data), re.findall('->\\s([A-Z])', data)))


def get_window(template: list) -> list[tuple[int, int]]:
    """Returns a list of tuples containing the index window (every 2).
    This is used to index into the template to get the polymer pair.
    """
    return [(i, i + 1) for i in range(len(template) - 1)]


def get_pairs(template: list) -> dict[str: int]:
    """Returns a dict of the number of pairs (key), and their count (value)."""
    pairs = [template[w[0]] + template[w[1]] for w in get_window(template)]
    counts = np.unique(pairs, return_counts=True)
    return dict(zip(counts[0], counts[1]))


def update_pairs(pairs: dict[str: int], rules: dict[str: int]) -> tuple[dict[str, int], dict[str, int]]:
    """Adds the new polymer as outlined in the rules for a polymer pair.
    Returns a dict of the new pairs created,
    plus the pairs that should be removed due to the insertion of new polymers.
    """
    new_pairs, pairs_to_remove = {}, {}

    for pair, value in pairs.items():  # Will add two new pairs, e.g. NN -> NC and CN, and remove NN.
        polymer = rules[pair]

        # Setting a dict of the new polymer pairs and their amount.
        if pair[0] + polymer in new_pairs:
            new_pairs[pair[0] + polymer] += value
        else:
            new_pairs[pair[0] + polymer] = value
        if polymer + pair[1] in new_pairs:
            new_pairs[polymer + pair[1]] += value
        else:
            new_pairs[polymer + pair[1]] = value

        # Setting a dict of pairs and the amount of times to be removed.
        if pair in pairs_to_remove:
            pairs_to_remove[pair] += value
        else:
            pairs_to_remove[pair] = value

    return new_pairs, pairs_to_remove


def grow_polymer(pairs: dict[str: int], rules: dict[str: int], steps: int) -> dict[str: int]:
    """Grows the polymer chain by inserting the new polymers into it, and removing the replaced pairs."""
    for i in range(steps):
        new_pairs, pairs_to_remove = update_pairs(pairs, rules)

        # Adding new polymer pairs to the template.
        for pair, value in new_pairs.items():
            if pair in pairs:
                pairs[pair] += value
            else:
                pairs[pair] = value

        # Removing the no longer present pairs.
        for pair, value in pairs_to_remove.items():
            pairs[pair] -= value
            if pairs[pair] <= 0:
                pairs.pop(pair)

    return pairs


def most_sub_least(steps: int, template: list[str], rules: dict[str: int]) -> int:
    """Returns the value of the most common element in the polymer template minus the least common,
    given the number of steps.
    """
    pairs = get_pairs(template)
    pairs = grow_polymer(pairs, rules, steps)

    # Count the values of the individual polymers.
    polymers = {pd: 0 for pd in set(p for p in rules.values())}
    for pair, value in pairs.items():
        polymers[pair[0]] += value

    # last value in the template won't have been counted just by counting the first part of a pair.
    polymers[template[-1]] += 1

    poly_list = sorted(polymers.items(), key=itemgetter(1))

    return poly_list[-1][1] - poly_list[0][1]


def main() -> None:
    data = get_data('data/14.txt')
    template = get_template(data)
    rules = get_insertion_rules(data)

    print(f'Part 1 solution is: { most_sub_least(10, template, rules) }')
    print(f'Part 2 solution is: { most_sub_least(40, template, rules) }')


if __name__ == "__main__":
    main()
