# sourcery skip: for-append-to-extend, list-comprehension
import re
from pathlib import Path
from typing import List

from rich import print
from tqdm import tqdm

with open(Path(__file__).parent / "testdata.txt") as file:
    _data = file.read().split("\n")
    order = []
    to_order = []
    for line in _data:
        if "|" in line:
            order.append(tuple(int(x) for x in line.split("|")))
        elif "," in line:
            to_order.append([int(x) for x in line.split(",")])

valid = []

for line in to_order:
    ordered = True
    for digit in line:
        order_to_check = []
        for orders in order:
            if digit in orders and (
                digit == orders[0]
                and orders[1] in line
                or digit != orders[0]
                and orders[0] in line
            ):
                order_to_check.append(orders)
        for check in order_to_check:
            idx1 = line.index(check[0])
            idx2 = line.index(check[1])
            if idx1 > idx2:
                ordered = False
                break
    if ordered:
        valid.append(line)
tot = 0
for line in valid:
    mid = len(line) // 2
    tot += line[mid]
print("Part 1:", tot)


# cleanup data for part 2
for line in valid:
    for _line in to_order:
        if line == _line:
            to_order.remove(_line)
            break
