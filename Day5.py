import re
rules = []
updates = []

with open("Day5.txt") as input:
    for line in input:
        if "|" in line:
            rules.append(line.strip())
        elif "," in line:
            pages = list(map(int, re.findall(r'\d+', line)))
            updates.append(pages)

total = 0
incorrect = []
for update in updates:
    faults = 0
    for i, page in enumerate(update):
        for k in range(i):
            if f"{update[i]}|{update[k]}" in rules:
                faults += 1
    if faults == 0:
        total += update[int((len(update)-1)/2)]
    else:
        incorrect.append(update)


print(f"Total of middle pages for valid updates: {total} ")

for update in incorrect:
    for i, page in enumerate(update):
        for k in range(i):
            if f"{update[i]}|{update[k]}" in rules:
                a = update[i]
                update.remove(a)
                update.insert(k, a)

total = 0
for update in incorrect:
    total += update[int((len(update)-1)/2)]

print(f"Total of middle pages for *invalid* updates: {total} ")
