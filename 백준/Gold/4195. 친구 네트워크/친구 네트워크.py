import sys
input = sys.stdin.readline

t = int(input())

def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]

def union(parent, size, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    
    if root_a != root_b:
        parent[root_b] = root_a
        size[root_a] += size[root_b]
        
    return size[root_a]    
    
for _ in range(t):
    F = int(input())
    parent = dict()
    size = dict()
    
    for _ in range(F):
        a, b = input().split()
        
        if a not in parent:
            parent[a] = a
            size[a] = 1
        if b not in parent:
            parent[b] = b
            size[b] = 1
            
        print(union(parent, size, a, b))    