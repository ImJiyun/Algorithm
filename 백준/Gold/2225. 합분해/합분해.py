N, K = map(int, input().split())

# count = 0
# def permute(arr):
#     global count
#     if len(arr) == K-1:
#         count += 1
#     for i in range(N+1):
#         permute(arr + [i])

# permute([])
# print(count)

MOD = 1_000_000_000
# dp[i][j] = i개의 수로 합이 j가 되는 경우의 수
dp = [[0] * (N+1) for _ in range(K+1)]

# 합이 0이 되는 방법은 전부 [0, 0, ..., 0] 딱 1개
for i in range(K+1):
    dp[i][0] = 1

for i in range(1, K+1):         # i개의 수
    for j in range(1, N+1):     # 합이 j
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % MOD

print(dp[K][N])  # K개의 수로 합이 N 되는 경우의 수