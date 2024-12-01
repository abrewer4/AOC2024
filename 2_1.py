from utils import *

lines = getLines("2_1.txt")


def isSafe(numberList):
    # are the numbers in the list always increasing/decreasing
    # return false if there is both an increase AND a decrease inbetween numbers in the list
    increases = 0
    decreases = 0
    for i in range(len(numberList)-1):
        a = int(numberList[i])
        b = int(numberList[i+1])
        if b > a:
            increases += 1
        elif b < a:
            decreases += 1
        else:
            return False

        if not (isGradualChange(a, b)):
            return False

        if min(increases, decreases) != 0:
            return False
    return True


def isGradualChange(a, b):
    # Change must be at least one and at most 3
    difference = max(a, b) - min(a, b)

    if difference > 3:
        return False
    elif difference < 1:
        return False
    else:
        return True


reportsList = []
for line in lines:
    reportsList.append(line.split(" "))
safe = 0
unsafe = 0
for line in reportsList:
    if isSafe(line):
        safe += 1
    else:
        unsafe += 1

print(f"Safe reports:   {safe}")
print(f"Unsafe reports: {unsafe}")
