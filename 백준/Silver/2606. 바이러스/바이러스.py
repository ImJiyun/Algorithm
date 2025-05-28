import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
    
arr = [[] for _ in range(N+1)]
    
for _ in range(M):
    a, b = map(int, input().split(" "))
    arr[a].append(b)
    arr[b].append(a)

visited = set()
count = 0
        
def dfs(node):
    global count
    visited.add(node)
    count += 1
    
    for nxt in arr[node]:
        if nxt not in visited:
            dfs(nxt)
            
dfs(1)
print(count - 1)