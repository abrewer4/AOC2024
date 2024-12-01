# Day 1 Part 2

# Calculate the 'difference between the two lists
# Sort them in ascending order and then find the difference between each pair
# Return the sum of the differences
# -------------------------
# Part 2:
# For each number in list a, multiply it by the number of occurrences in list b
# Return the total of these 'similarity scores' for list a

alist = []
blist = []

with open("1_1.txt") as input:
    for line in input:
        a = line.split(" ")[0]
        b = line.split(" ")[-1]

        alist.append(int(a))
        blist.append(int(b))
# alist.sort()
# blist.sort()

# distance = 0

# for (a, b) in zip(alist, blist):
#     distance += max(a, b)-min(a, b)

# print(f"Total distance: {distance}")
similarity = 0

for item in alist:
    count = 0
    for other in blist:
        if item == other:
            count += 1
    similarity += item * count

print(f"Total list similarity: {similarity}")
