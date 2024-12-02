from rich import print
from pathlib import Path

data = []
path = Path(__file__).parent / "data.txt"
with open(path, "r") as file:
    for line in file:
        data.append((int(line.split(" ")[0]), int(line.split(" ")[-1])))

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
for i in range(len(list1)):
    count = list2.count(list1[i])
    dist = list1[i]*count
    s += dist
print("part 2:", s)