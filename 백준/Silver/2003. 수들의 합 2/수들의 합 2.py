import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
left, right, total = 0, 0, 0

while right < N:
    total += A[right]
    while total > M:
        total -= A[left]
        left += 1
    if total == M:
        cnt += 1
    right += 1

print(cnt)