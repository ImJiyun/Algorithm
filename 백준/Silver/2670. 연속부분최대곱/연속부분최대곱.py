import sys
input = sys.stdin.readline

N = int(input())
arr = [float(input().strip()) for _ in range(N)]
    
dp = [0] * N
dp[0] = arr[0]

for i in range(1, N):
    dp[i] = max(arr[i], dp[i-1] * arr[i])
    
print(f"{max(dp):.3f}")    