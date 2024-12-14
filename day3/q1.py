from rich import print
from typing import List
import re
from tqdm import tqdm
from pathlib import Path

with open(Path(__file__).parent / "data.txt") as file:
    data = file.read()


REGEX = r"mul\(\d+\,\d+\)"
DONT_RE = r"don't()"
DO_RE = r"do()"

can_mul = True
s = 0
matches = re.findall(REGEX, data)
for match in tqdm(matches):
    num1 = int(match.split("(")[1].split(",")[0])
    num2 = int(match.split(",")[1].split(")")[0])
    s += num1 * num2
print("part 1:", s)

s = 0
COMBINED_RE = r"mul\(\d+\,\d+\)|don't\(\)|do\(\)"
matches = re.findall(COMBINED_RE, data)
can_mul = True
for match in tqdm(matches):
    if match == DONT_RE:
        can_mul = False
        continue
    elif match == DO_RE:
        can_mul = True
        continue
    elif can_mul:
        num1 = int(match.split("(")[1].split(",")[0])
        num2 = int(match.split(",")[1].split(")")[0])
        s += num1 * num2
print("part 2:", s)