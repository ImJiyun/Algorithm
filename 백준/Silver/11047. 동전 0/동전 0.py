import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
A.sort(reverse=True)

ans = 0

for coin in A:
    if K == 0:
        break
    if coin > K:
        continue
    cnt = K // coin
    ans += cnt
    K -= coin * cnt
      
print(ans)        