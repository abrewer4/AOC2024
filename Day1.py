alist = []
blist = []

with open("Day1.txt") as input:
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

# ------------ PART 2 -----------------

similarity = 0

for item in alist:
    count = 0
    for other in blist:
        if item == other:
            count += 1
    similarity += item * count

print(f"Total list similarity: {similarity}")
