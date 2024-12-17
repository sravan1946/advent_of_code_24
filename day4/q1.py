import re
from pathlib import Path
from typing import List

from rich import print
from tqdm import tqdm

with open(Path(__file__).parent / "testdata.txt") as file:
    temp_data = file.read().split("\n")
    data = [list(line) for line in temp_data]
for i in data:
    print(i)

h = 0
ve = 0
d = 0
for line_no, line in enumerate(data):
    for index, v in enumerate(line):
        if index >= len(line) - 3:
            break
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
            break
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
            break
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
            d += 1

    for index, v in enumerate(line):
        if index <= 3 or line_no >= len(data) - 3:
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
            print(
                v,
                data[line_no + 1][index - 1],
                data[line_no + 2][index - 2],
                data[line_no + 3][index - 3],
                line_no,
                index,
            )
            d += 1
print("h:", h)
print("ve:", ve)
print("d:", d)
print("total: ", h + ve + d)
