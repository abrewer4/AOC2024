import re


def extractInstructions(inputString):
    return re.findall(r'mul\(\d+\,\d+\)', str(inputString))


def parseInstructions(inputList):
    total = 0
    for instruction in inputList:
        a, b = map(int, re.findall(r'\d+', instruction))
        total += a*b
    return total


with open("3.txt") as input:
    fileString = input.read()

instructions = extractInstructions(fileString)

total = 0

total += parseInstructions(instructions)
print(f"Total of *all* valid multiplications: {total}")

# ---------------- PART 2 -------------------------------

# THE LINE BREAKS WERE MAKING THE REGEX MISS MATCHES :(((
singleLine = ""
for line in fileString:
    singleLine += str(line).strip()

enabledSections = re.findall(
    r"(((do\(\))|^).+?(?=don't\(\))|$)|(do\(\)).+", singleLine)

total = 0

for section in enabledSections:
    instructions = extractInstructions(section)
    total += parseInstructions(instructions)

print(f"Total of *enabled* valid multiplications: {total}")
