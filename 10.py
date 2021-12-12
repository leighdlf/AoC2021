def main():
    with open("10.txt") as file:
        data = [line.strip() for line in file.readlines()]

    open_close_dict = {'(': ')', '[': ']', '{': '}', '<': '>'}
    illegal_score_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}
    completion_score_dict = {')': 1, ']': 2, '}': 3, '>': 4}

    incomplete_lines = []  # Lines that are not corrupt but incomplete.

    def syntax_error_score():
        """Returns the total syntax error score for corrupt lines.
        It also updates the incomplete_line list.
        """
        illegal_characters = []
        for line in data:
            opening_list = []
            add_incomplete_flag = True  # Used to break out of inner loop.
            for character in line:
                if character in open_close_dict:
                    opening_list.append(character)
                else:
                    if open_close_dict[opening_list[-1]] == character:
                        opening_list.pop()
                    else:
                        illegal_characters.append(character)
                        add_incomplete_flag = False
                        break
            if add_incomplete_flag:
                incomplete_lines.append(opening_list)

        return sum([illegal_score_dict[character] for character in illegal_characters])

    print(syntax_error_score())

    def completion_scores():
        """Returns the middle score for the closing of incomplete lines."""
        all_scores = []
        for line in incomplete_lines:
            score = 0
            for i in range(len(line)):  # Iterate over line in reverse order.
                point = completion_score_dict[open_close_dict[line[-(i + 1)]]]
                score = score * 5 + point
            all_scores.append(score)

        all_scores.sort()
        return all_scores[len(all_scores) // 2]

    print(completion_scores())


if __name__ == "__main__":
    main()
