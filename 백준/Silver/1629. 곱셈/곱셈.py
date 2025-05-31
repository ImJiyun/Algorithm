import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())

def cal(a, b):
    if b == 1:
        return a % C
    n = cal(a, b // 2)
    if b % 2 == 0:
        return n * n % C
    else:
        return n * n * a % C
print(cal(A, B))