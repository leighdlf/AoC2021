import numpy as np


def main(part):
    first_or_last_board = True if part == 1 else False

    with open("04.txt") as file:
        # Opening the file and setting up the boards as a nDimensional np.array.
        content = file.readlines()
        numbers = [int(n) for n in content[0].split(',')]
        board_list = [[int(n) for n in b.split()] for b in content[2:] if b != '\n']
        num_boards = len(board_list) // 5
        num_nums = len(numbers)
        boards = np.array(board_list).reshape((num_boards, 5, 5))

    # Setting up the variables needed.
    marked = np.zeros((num_boards, 5, 5), dtype=int)  # Change to 1 when marked.
    boards_won = []
    winning_sums = []

    def mark(n):
        for z in range(num_boards):
            if z in boards_won:  # If the board has won don't bother marking.
                continue
            for y in range(5):
                for x in range(5):
                    if boards[z, y, x] == n:
                        marked[z, y, x] = 1

    def check_win():
        for board_index in range(num_boards):
            if board_index in boards_won:  # Don't need to check if it's already won.
                continue
            for i in range(5):
                if sum(marked[board_index, i, 0:]) == 5:  # Horizontal.
                    boards_won.append(board_index)
                    winning_sums.append(return_sum(board_index))
                    continue  # If board has won horizontally don't need to check vertically.
                if sum(marked[board_index, 0:, i]) == 5:  # Vertical.
                    boards_won.append(board_index)
                    winning_sums.append(return_sum(board_index))

    def return_sum(winning_index):
        not_marked = []
        for y in range(5):
            for x in range(5):
                if not marked[winning_index, y, x]:
                    not_marked.append(boards[winning_index, y, x])
        return sum(not_marked) * number

    # Main loop/logic.
    for number in numbers:
        mark(number)
        check_win()

    if first_or_last_board:  # First or last values depending on the question.
        return winning_sums[0]
    else:
        return winning_sums.pop()


if __name__ == "__main__":
    print(main(1))
    print(main(2))
