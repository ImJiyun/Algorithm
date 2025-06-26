import sys
input = sys.stdin.readline

n, m = map(int, input().split())
    
parent = [i for i in range(n+1)]    

def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

def union(a, b):
    parent[find(b)] = find(a)

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b)
    else:
        if find(b) == find(a):
            print('YES')
        else:
            print('NO')