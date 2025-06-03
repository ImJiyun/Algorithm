def solution(k, dungeons):
    N = len(dungeons)
    visited = [False] * N
    maxCnt = [0]
    
    def dfs(curE, cnt):
        maxCnt[0] = max(cnt, maxCnt[0])
        
        for i in range(N):
            if not visited[i] and curE >= dungeons[i][0]:
                visited[i] = True
                dfs(curE - dungeons[i][1], cnt + 1)
                visited[i] = False
                
    dfs(k, 0)
    return maxCnt[0]