
lines = []
with open("Day2.txt") as input:
    for line in input:
        lines.append(line.strip())


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

# ----------- PART 2 ----------------


def removeNthItem(list, n):
    newList = []
    for i, item in enumerate(list):
        if i == n:
            pass
        else:
            newList.append(item)
    return newList


def reduceReportForEach(list):
    newLists = []
    for i in range(len(list)):
        newLists.append(removeNthItem(list, i))

    return newLists


safe = 0
unsafe = 0

for line in reportsList:
    if isSafe(line):
        safe += 1
        # print(f"✔️  SAFE: {line}")
    else:
        reducedReports = reduceReportForEach(line)
        safeRRs = 0
        for RR in reducedReports:
            if isSafe(RR):
                safeRRs += 1
                # print(f"Dampened-> {RR}")
        if safeRRs > 0:
            safe += 1
            # print(f"✔️  SAFE: {line}")
        else:
            unsafe += 1
            # print(f"❌UNSAFE: {line}")
print("\nAfter engaging the problem dampener...")
print(f"Safe reports:   {safe}")
print(f"Unsafe reports: {unsafe}")
