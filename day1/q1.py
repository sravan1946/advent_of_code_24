from pathlib import Path

from rich import print

data = []
path = Path(__file__).parent / "data.txt"
with open(path, "r") as file:
    data.extend((int(line.split(" ")[0]), int(line.split(" ")[-1])) for line in file)
list1 = [x[0] for x in data]
list2 = [x[1] for x in data]
list1.sort()
list2.sort()
s = 0
for i in range(len(list1)):
    dist = abs(list1[i] - list2[i])
    s += dist
print("part 1:", s)

s = 0
for item in list1:
    count = list2.count(item)
    dist = item * count
    s += dist
print("part 2:", s)
