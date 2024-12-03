
def getInputLines(file):
    lines = []
    with open(file) as input:
        for line in input:
            lines.append(line.strip())

    return lines


def printSample(input, lines=3):
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

    printSample(inputLines, 5)

    partOne()
    # partTwo()


def difference(a, b):
    return max(a, b) - min(a, b)


def tests():
    Q = [[1, 2], [12, 4], [-1, 5], [0, -12], [4, -9], [1, 6.5]]
    A = [1, 8, 6, 12, 13, 5.5]
    for q, a in zip(Q, A):
        assert difference(*q) == a, f"Difference of {q} should be {a}"


if __name__ == "__main__":
    tests()
    main()
