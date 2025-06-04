def solution(cards):
    N = len(cards)
    visited = [False] * (N)
    ans = []
    
    def dfs(i):
        cnt[0] += 1
        visited[i] = True
        
        if not visited[cards[i]-1]:
            dfs(cards[i]-1)
        
    for i in range(len(cards)):
        if not visited[i]:
            cnt = [0]
            dfs(i)
            ans.append(cnt[0])
            
    ans.sort(reverse=True)
    
    return ans[0] * ans[1] if len(ans) >= 2 else 0