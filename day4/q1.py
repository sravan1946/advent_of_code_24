import re
from pathlib import Path
from typing import List

from rich import print
from tqdm import tqdm

with open(Path(__file__).parent / "testdata.txt") as file:
    temp_data = file.read().split("\n")
    data = [list(line) for line in temp_data]

h = 0
ve = 0
d1 = 0
d2 = 0
for line_no, line in tqdm(enumerate(data)):
    for index, v in enumerate(line):
        if index >= len(line) - 3:
            continue
        if (
            v == "X"
            and line[index + 1] == "M"
            and line[index + 2] == "A"
            and line[index + 3] == "S"
        ) or (
            v == "S"
            and line[index + 1] == "A"
            and line[index + 2] == "M"
            and line[index + 3] == "X"
        ):
            h += 1

    for index, v in enumerate(line):
        if line_no >= len(data) - 3:
            continue
        if (
            v == "X"
            and data[line_no + 1][index] == "M"
            and data[line_no + 2][index] == "A"
            and data[line_no + 3][index] == "S"
        ) or (
            v == "S"
            and data[line_no + 1][index] == "A"
            and data[line_no + 2][index] == "M"
            and data[line_no + 3][index] == "X"
        ):
            ve += 1

    for index, v in enumerate(line):
        if index >= len(line) - 3 or line_no >= len(data) - 3:
            continue
        if (
            v == "X"
            and data[line_no + 1][index + 1] == "M"
            and data[line_no + 2][index + 2] == "A"
            and data[line_no + 3][index + 3] == "S"
        ) or (
            v == "S"
            and data[line_no + 1][index + 1] == "A"
            and data[line_no + 2][index + 2] == "M"
            and data[line_no + 3][index + 3] == "X"
        ):
            # print(v, data[line_no + 1][index + 1], data[line_no + 2][index + 2], data[line_no + 3][index + 3], line_no, index)
            d1 += 1

    for index, v in enumerate(line):
        if  line_no >= len(data) - 3 or index <= 2:
            continue
        # print(line_no, len(data), index, len(line))
        if (
            v == "X"
            and data[line_no + 1][index - 1] == "M"
            and data[line_no + 2][index - 2] == "A"
            and data[line_no + 3][index - 3] == "S"
        ) or (
            v == "S"
            and data[line_no + 1][index - 1] == "A"
            and data[line_no + 2][index - 2] == "M"
            and data[line_no + 3][index - 3] == "X"
        ):
            # print(
            #     v,
            #     data[line_no + 1][index - 1],
            #     data[line_no + 2][index - 2],
            #     data[line_no + 3][index - 3],
            #     line_no,
            #     index,
            # )
            d2 += 1


print("h:", h)
print("ve:", ve)
print("d1:", d1)
print("d2:", d2)
print("total part1: ", h + ve + d1 + d2)


mas = 0

for line_no, line in tqdm(enumerate(data)):
    for index, v in enumerate(line):
        if (line_no == 0) or (index == 0) or (line_no == len(data) - 1) or (index == len(line) - 1):
            print("skipping", line_no, index)
            continue
        if (line_no == 7):
            print(line_no, index)
        if (
            v == "A"
            and (
                data[line_no - 1][index-1] == "M" and data[line_no + 1][index+1] == "S"
                or data[line_no - 1][index-1] == "S" and data[line_no + 1][index+1] == "M"
            )
            and (
                data[line_no - 1][index+1] == "M" and data[line_no + 1][index-1] == "S"
                or data[line_no - 1][index+1] == "S" and data[line_no + 1][index-1] == "M"
            )
        ):
            print("found", line_no, index)
            mas += 1
print("mas:", mas)