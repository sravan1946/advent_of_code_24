from rich import print
from typing import List
import re
from tqdm import tqdm
from pathlib import Path

with open(Path(__file__).parent / "testdata.txt") as file:
    temp_data = file.read().split("\n")
    data = []
    for line in temp_data:
        data.append(list(line))
s = 0

# WORD IS XMAS or SAMX
def word_in_hori(data: List[str]) -> bool:
    for i in range(len(data)):
        if i == 0 and (data[i] == "S" or data[i] == "X"):
            if data[i] == "S" and data[i+1] == "A" and data[i+2] == "M" and data[i+3] == "X":
                return True
            elif data[i] == "X" and data[i+1] == "M" and data[i+2] == "A" and data[i+3] == "S":
                return True
        elif i == len(data) - 1 and (data[i] == "S" or data[i] == "X"):
            if data[i] == "S" and data[i-1] == "A" and data[i-2] == "M" and data[i-3] == "X":
                return True
            elif data[i] == "X" and data[i-1] == "M" and data[i-2] == "A" and data[i-3] == "S":
                return True
        elif i != 0 and i != len(data) - 1 and (data[i] == "S" or data[i] == "X"):
            if data[i] == "S" and data[i+1] == "A" and data[i+2] == "M" and data[i+3] == "X":
                return True
            elif data[i] == "X" and data[i+1] == "M" and data[i+2] == "A" and data[i+3] == "S":
                return True
            if data[i] == "S" and data[i-1] == "A" and data[i-2] == "M" and data[i-3] == "X":
                return True
            elif data[i] == "X" and data[i-1] == "M" and data[i-2] == "A" and data[i-3] == "S":
                return True
    return False

def count_vertical(data: List[List[str]]) -> int:
    s = 0
    for i in range(len(data[0])):
        for j in range(len(data)):
            if j == 0 and (data[j][i] == "S" or data[j][i] == "X"):
                if data[j][i] == "S" and data[j+1][i] == "A" and data[j+2][i] == "M" and data[j+3][i] == "X":
                    s += 1
                elif data[j][i] == "X" and data[j+1][i] == "M" and data[j+2][i] == "A" and data[j+3][i] == "S":
                    s += 1
            elif j == len(data) - 1 and (data[j][i] == "S" or data[j][i] == "X"):
                if data[j][i] == "S" and data[j-1][i] == "A" and data[j-2][i] == "M" and data[j-3][i] == "X":
                    s += 1
                elif data[j][i] == "X" and data[j-1][i] == "M" and data[j-2][i] == "A" and data[j-3][i] == "S":
                    s += 1
            elif j != 0 and j != len(data) - 1 and (data[j][i] == "S" or data[j][i] == "X"):
                if data[j][i] == "S" and data[j+1][i] == "A" and data[j+2][i] == "M" and data[j+3][i] == "X":
                    s += 1
                elif data[j][i] == "X" and data[j+1][i] == "M" and data[j+2][i] == "A" and data[j+3][i] == "S":
                    s += 1
                if data[j][i] == "S" and data[j-1][i] == "A" and data[j-2][i] == "M" and data[j-3][i] == "X":
                    s += 1
                elif data[j][i] == "X" and data[j-1][i] == "M" and data[j-2][i] == "A" and data[j-3][i] == "S":
                    s += 1
    return s

def count_diagonal(data: List[List[str]]) -> int:
    s = 0
    for i in range(len(data[0])):
        for j in range(len(data)):
            try:
                if j == 0 and (data[j][i] == "S" or data[j][i] == "X"):
                    if data[j][i] == "S" and data[j+1][i+1] == "A" and data[j+2][i+2] == "M" and data[j+3][i+3] == "X":
                        s += 1
                    elif data[j][i] == "X" and data[j+1][i+1] == "M" and data[j+2][i+2] == "A" and data[j+3][i+3] == "S":
                        s += 1
                elif j == len(data) - 1 and (data[j][i] == "S" or data[j][i] == "X"):
                    if data[j][i] == "S" and data[j-1][i-1] == "A" and data[j-2][i-2] == "M" and data[j-3][i-3] == "X":
                        s += 1
                    elif data[j][i] == "X" and data[j-1][i-1] == "M" and data[j-2][i-2] == "A" and data[j-3][i-3] == "S":
                        s += 1
                elif j != 0 and j != len(data) - 1 and (data[j][i] == "S" or data[j][i] == "X"):
                    if data[j][i] == "S" and data[j+1][i+1] == "A" and data[j+2][i+2] == "M" and data[j+3][i+3] == "X":
                        s += 1
                    elif data[j][i] == "X" and data[j+1][i+1] == "M" and data[j+2][i+2] == "A" and data[j+3][i+3] == "S":
                        s += 1
                    if data[j][i] == "S" and data[j-1][i-1] == "A" and data[j-2][i-2] == "M" and data[j-3][i-3] == "X":
                        s += 1
                    elif data[j][i] == "X" and data[j-1][i-1] == "M" and data[j-2][i-2] == "A" and data[j-3][i-3] == "S":
                        s += 1
            except IndexError:
                pass
    return s


for d in data:
    if word_in_hori(d):
        s += 1
    print(d + [word_in_hori(d)])

print(count_vertical(data))
print(count_diagonal(data))


print(s)