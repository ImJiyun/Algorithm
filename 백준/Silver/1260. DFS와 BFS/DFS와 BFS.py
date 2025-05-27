import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split(" "))

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b= map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, N+1):
    graph[i].sort()

visited = [False] * (N+1)

def dfs(node):
    print(node, end=" ")
    visited[node] = True
    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(nxt)

def bfs(start):
    visited = [False] * (N+1)
    q = deque([start])
    visited[start] = True
    
    
    while q:
        curr = q.popleft()
        print(curr, end= " ")
        for nxt in graph[curr]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True

dfs(V)
print()
bfs(V)