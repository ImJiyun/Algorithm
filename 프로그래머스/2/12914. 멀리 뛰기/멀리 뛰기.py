def solution(n):
    dp = [0] * (n+1)
    dp[0] = 1
    
    for i in range(1, n+1):
        for k in range(1, 3):
            if i - k >= 0:
                dp[i] = (dp[i] + dp[i-k]) % 1234567
                
    return dp[n]