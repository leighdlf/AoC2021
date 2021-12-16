def main(part):
    with open('data/08.txt') as file:
        signal_patterns = \
            [
                [[set(p for p in pattern) for pattern in patterns.strip().split()]
                 for patterns in line.split('|')] for line in file.readlines()
            ]

    if part == 1:
        count = 0
        for j in range(len(signal_patterns)):
            for value in signal_patterns[j][1]:
                if len(value) in (2, 3, 4, 7):
                    count += 1
        print(count)

    if part == 2:
        output_list = []
        for i in range(len(signal_patterns)):

            output_values = signal_patterns[i][1]
            unique_signals = signal_patterns[i][0]

            # filtering of the unique signals to ge the values that are initially knowable.
            one = list(filter(lambda x: len(x) == 2, unique_signals))[0]
            four = list(filter(lambda x: len(x) == 4, unique_signals))[0]
            seven = list(filter(lambda x: len(x) == 3, unique_signals))[0]
            eight = list(filter(lambda x: len(x) == 7, unique_signals))[0]
            two_three_five = list(filter(lambda x: len(x) == 5, unique_signals))
            zero_six_nine = list(filter(lambda x: len(x) == 6, unique_signals))

            # Set operations to map input to correct output segments.
            a = seven - one
            b_d = four - one
            e_g = (eight - four) - a
            b = [(b_d - x) for x in two_three_five if len(b_d.difference(x)) == 1][0]
            d = b_d - b
            e = [(e_g - x) for x in zero_six_nine if len(e_g.difference(x)) == 1][0]
            g = e_g - e
            c = [(one - x) for x in zero_six_nine if len(one.difference(x)) == 1][0]
            f = one - c
            zero = {segment.copy().pop() for segment in [a, b, c, e, f, g]}
            two = {segment.copy().pop() for segment in [a, c, d, e, g]}
            three = {segment.copy().pop() for segment in [a, c, d, f, g]}
            five = {segment.copy().pop() for segment in [a, b, d, f, g]}
            six = {segment.copy().pop() for segment in [a, b, d, e, f, g]}
            nine = {segment.copy().pop() for segment in [a, b, c, d, f, g]}

            # Matching cases.
            every_entry = ''
            for value in output_values:
                value_str = ''
                if value == zero:
                    value_str = '0'
                elif value == one:
                    value_str = '1'
                elif value == two:
                    value_str = '2'
                elif value == three:
                    value_str = '3'
                elif value == four:
                    value_str = '4'
                elif value == five:
                    value_str = '5'
                elif value == six:
                    value_str = '6'
                elif value == seven:
                    value_str = '7'
                elif value == eight:
                    value_str = '8'
                elif value == nine:
                    value_str = '9'
                every_entry += value_str

            output_list.append(int(every_entry))

        print(sum(output_list))


if __name__ == "__main__":
    main(1)
    main(2)
