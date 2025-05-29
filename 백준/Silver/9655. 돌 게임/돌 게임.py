# 3 1 1
import sys

input = sys.stdin.readline

N = int(input())

a = N // 3
b = N % 3

print('CY') if (a + b) % 2 == 0 else print('SK')