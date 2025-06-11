import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
right, total = 0, 0

for left in range(N):
    while total < M and right < N:
        total += A[right]
        right += 1
    if total == M:
        cnt += 1
    total -= A[left]
    
print(cnt)