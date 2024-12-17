from pathlib import Path

from rich import print
from tqdm import tqdm

with open(Path(__file__).parent / "data.txt") as file:
    data = [list(map(int, line.strip().split())) for line in file]


def is_asc(data: list[int]) -> bool:
    return all(data[i] >= data[i + 1] for i in range(len(data) - 1))


def is_dec(data: list[int]) -> bool:
    return all(data[i] <= data[i + 1] for i in range(len(data) - 1))


def is_safe(data: list[int]) -> bool:
    if not is_asc(data) and not is_dec(data):
        return False
    return not any(
        0 < abs(data[i] - data[i + 1]) > 3 or abs(data[i] - data[i + 1]) == 0
        for i in range(len(data) - 1)
    )


count = sum(bool(is_safe(li)) for li in tqdm(data, desc="part 1"))
print("part 1:", count)

count = 0
for li in tqdm(data, desc="part 2"):
    idx = 0
    if is_safe(li):
        count += 1
    while not is_safe(li):
        popped = li.pop(idx)
        if is_safe(li):
            count += 1
            break
        else:
            li.insert(idx, popped)
        idx += 1
        if idx == len(li):
            break
print("part 2:", count)
