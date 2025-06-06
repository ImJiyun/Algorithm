from collections import deque, defaultdict

def solution(n, edge):
    adj = defaultdict(list)
    
    for a, b in edge:
        adj[a].append(b)
        adj[b].append(a)
        
    visited = [False] * (n+1)
    
    q = deque([1])
    visited[1] = True
    
    while q:
        size = len(q)
        for _ in range(size):
            cur = q.popleft()

            for nxt in adj[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
     
    return size