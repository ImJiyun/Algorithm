import sys
input = sys.stdin.readline

N, M = map(int, input().split())

ans = []
visited = [False] * (N+1)

def permute():
    if len(ans) == M:
        print(' '.join(map(str, ans)))
        return
        
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = True
        ans.append(i)
        permute()
        ans.pop()
        visited[i] = False
        
permute()        