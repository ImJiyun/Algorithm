import sys 
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

arr = []
visited = [False] * N
max_value = 0

def dfs():
    global max_value
    if len(arr) == N:
        total = 0
        for i in range(N-1):
            total += abs(arr[i] - arr[i+1])
        max_value = max(max_value, total)
        return
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True  
        arr.append(A[i])
        dfs()    
        arr.pop()
        visited[i] = False
dfs()        
print(max_value)        