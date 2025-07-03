def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)] 
    dp[0][0] = 1
    
    puddles = set((y-1, x-1) for [x, y] in puddles)
    MOD = 1_000_000_007
    
    for r in range(n):
        for c in range(m):
            if (r, c) in puddles:
                continue
                
            if r == 0 and c == 0:
                continue
            elif r == 0:    
                dp[r][c] = dp[r][c-1] % MOD
            elif c == 0:
                dp[r][c] = dp[r-1][c] % MOD
            else:
                dp[r][c] = (dp[r-1][c] + dp[r][c-1]) % MOD
                
    return dp[n-1][m-1]