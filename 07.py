def main():
    with open('test.txt') as file:
        data = [int(n) for n in file.read().split(sep=',')]


if __name__ == "__main__":
    main()