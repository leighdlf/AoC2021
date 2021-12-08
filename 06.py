def main(days):
    with open('06.txt') as file:
        ages = [int(n) for n in file.read().split(sep=',')]

    # index 0 to 8 represent the days, value the number of fish.
    fish_per_day = [0 for _ in range(9)]
    for age in ages:
        fish_per_day[age] += 1

    for day in range(days):
        new_fish = fish_per_day[0]  # Caching this value.
        for i in range(8):
            fish_per_day[i] = fish_per_day[i + 1]
        fish_per_day[6] += new_fish  # Fish having their timer reset.
        fish_per_day[8] = new_fish  # New fish created.

    print(sum(fish_per_day))


if __name__ == "__main__":
    main(80)
    main(256)
