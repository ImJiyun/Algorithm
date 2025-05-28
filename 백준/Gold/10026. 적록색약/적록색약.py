import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    arr.append(list(input().strip()))

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(r, c, type):
    visited.add((r, c))
    for dr, dc in dir:
        nr, nc = r + dr, c + dc
        if nr < 0 or nc < 0 or nr >= N or nc >= N:
            continue
        if (nr, nc) in visited:
            continue
        if type == 0:
            if arr[r][c] == arr[nr][nc]:
                dfs(nr, nc, type)
        else:
            if arr[r][c] == arr[nr][nc] or (arr[r][c] in 'RG' and arr[nr][nc] in 'RG'):
                dfs(nr, nc, type)

visited = set()
count = 0
for r in range(N):
    for c in range(N):
        if (r, c) not in visited:
            dfs(r, c, 0)
            count += 1
print(count, end=" ")

visited = set()
count = 0
for r in range(N):
    for c in range(N):
        if (r, c) not in visited:
            dfs(r, c, 1)
            count += 1
print(count)
