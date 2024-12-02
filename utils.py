
def getLines(file):
    linesArray = []

    with open(file) as input:
        for line in input:
            linesArray.append(line.strip())

    return linesArray
