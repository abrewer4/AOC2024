
def getLines(file):
    linesArray = []

    with open(file) as input:
        for line in input:
            linesArray.append(line[0:-1])

    return linesArray
