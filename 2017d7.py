import re
sample = "Step C must be finished before step A can begin.\n Step C must be finished before step F can begin.\n Step A must be finished before step B can begin.\n Step A must be finished before step D can begin.\n Step B must be finished before step E can begin.\n Step D must be finished before step E can begin.\n Step F must be finished before step E can begin."


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
    return input[0:lines]


def partOne():
    answer = "???"

    print("")
    print(f"Part 1 answer is {answer}")


def partTwo():
    answer = "???"

    print("")
    print(f"Part 2 answer is {answer}")


def getDependentSteps(input):
    dependentSteps = {}

    # sample = printSample(inputLines, 5)
    for line in input.split("\n"):
        a, b = re.findall("\s([A-Z])\s", line)
        # print(f"Step {a} required for step {b}")
        if not (a in dependentSteps):
            dependentSteps[a] = [b]
        else:
            dependentSteps[a].append(b)
    return dependentSteps


def getChildren(a, dependentSteps):
    children = []
    for child in dependentSteps[a]:
        children.append(child)
    return children


def getParents(a, dependentSteps):
    parents = []
    for k in dependentSteps.keys():
        # print(dependentSteps[k])
        if a in dependentSteps[k]:
            parents.append(k)
    return parents


def main():
    inputLines = getInputLines("2017d7.txt")

    dependentSteps = getDependentSteps(sample)

    def isFirstNode(node):
        for b in dependentSteps:
            if node in dependentSteps[b]:
                return False
        return True

    done = []
    available = []
    waiting = []
    sequence = ""

    for a in dependentSteps:
        if isFirstNode(a):
            done.append(a)
            current = a
            print(f"{a} is the first step")

    def step(node, done, available, sequence, current, dependents):
        sequence += f" > {node}"
        done.append(node)

        oldList = available
        newList = []
        for item in oldList:
            if item in done:
                pass
            else:
                newList.append(item)
        available = newList

        for child in getChildren(node, dependents):
            if child in available:
                pass
            else:
                available.append(child)

        options = []
        waiting = False
        for option in available:
            for parent in getParents(option, dependents):
                if parent in done:
                    pass
                else:
                    waiting = True
            if waiting:
                pass
            else:
                options.append(option)

        print(options)
        print(available)
    # print(dependentSteps)
    # print(getParents("B"))
    step("C", done, available, sequence, current, dependentSteps)
    print(available)

    partOne()
    # partTwo()


def difference(a, b):
    return max(a, b) - min(a, b)


def tests():
    Q = [[1, 2], [12, 4], [-1, 5], [0, -12], [4, -9], [1, 6.5]]
    A = [1, 8, 6, 12, 13, 5.5]
    for q, a in zip(Q, A):
        assert difference(*q) == a, f"Difference of {q} should be {a}"
    assert getDependentSteps(sample) == {"C": ["A", "F"], "A": [
        "B", "D"], "B": ["E"], "D": ["E"], "F": ["E"]}
    assert getChildren("A", getDependentSteps(sample)) == ["B", "D"]
    assert getParents("A", getDependentSteps(sample)) == ["C"]
    # getParents("A", getDependentSteps(sample))


if __name__ == "__main__":
    tests()
    main()
