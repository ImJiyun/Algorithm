# 3 1 1
import sys

input = sys.stdin.readline

N = int(input())

stones = []

while N > 0:
    if N >= 3:
        stones.append(3)
        N -= 3
    else:
        stones.append(1)
        N -= 1

if len(stones) % 2 == 0:
    print('CY')
else:
    print('SK')