
lines = []
with open("Day4.txt") as input:
    for line in input:
        lines.append(line.strip())

keys = ["XMAS", "SAMX"]
diagonals = []
slanogaid = []
verticals = []

# lines = ["MMMSXXMASM", "MSAMXMSMSA", "AMXSXMAAMM", "MSAMASMSMX", "XMASAMXAMM",
#          "XXAMMXXAMA", "SMSMSASXSS", "SAXAMASAAA", "MAMMMXMMMM", "MXMXAXMASX"]

m = len(lines[0])
n = len(lines)

for x in range(m):
    vertical = ""
    for line in lines:
        vertical += line[x]
    verticals.append(vertical)

    diagonal = ""
    lanogaid = ""
    i = 0
    while x+i < m:
        diagonal += lines[i][x+i]
        lanogaid += lines[i][m-x-i-1]
        i += 1
    diagonals.append(diagonal)
    slanogaid.append(lanogaid)

y = 1

while y < n:
    diagonal = ""
    lanogaid = ""
    i = 0
    while y+i < n:
        diagonal += lines[y+i][i]
        lanogaid += lines[y+i][n-i-1]
        i += 1
    y += 1
    diagonals.append(diagonal)
    slanogaid.append(lanogaid)

count = 0

for direction in [lines, verticals, diagonals, slanogaid]:
    n = 0
    for line in direction:
        for key in keys:
            n += line.count(key)

    count += n
    print(f"XMAS found {n} times in 1d")


print(f"XMAS found {count} times")

crossCount = 0

for j in range(m-2):
    for k in range(m-2):
        chars = ""
        for a, b in zip([0, 0, 1, 2, 2], [0, 2, 1, 0, 2]):
            chars += lines[j+a][k+b]
        if chars in ["MSAMS", "MMASS", "SSAMM", "SMASM"]:
            crossCount += 1

print(f"XMAS cross found {crossCount} times")
