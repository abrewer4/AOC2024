# Day 1 Part 1

alist = []
blist = []

with open("1_1.txt") as input:
    for line in input:
        a = line.split(" ")[0]
        b = line.split(" ")[-1]

        alist.append(int(a))
        blist.append(int(b))
alist.sort()
blist.sort()

distance = 0

for (a, b) in zip(alist, blist):
    distance += max(a, b)-min(a, b)

print(f"Total distance: {distance}")