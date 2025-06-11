N = int(input())

right, total, cnt = 1, 0, 0

for left in range(1, N + 1):
    while total < N and right <= N:
        total += right
        right += 1
    if total == N:
        cnt += 1
    total -= left
print(cnt)