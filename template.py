
def getInputLines(file):
    lines = []
    with open("file.txt") as input:
        for line in input:
            lines.append(line.strip())

    return lines


def printSample(input, lines):
    print(f"First {lines} lines of input:")
    for i in range(min(len(input), lines)):
        print(input[i])


def partOne():
    answer = "???"

    print("")
    print(f"Part 1 answer is {answer}")


def partTwo():
    answer = "???"

    print("")
    print(f"Part 2 answer is {answer}")


def main():
    inputLines = getInputLines("1_1.txt")

    printSample(inputLines, 3)

    partOne()
    # partTwo()


if __name__ == "__main__":
    main()
