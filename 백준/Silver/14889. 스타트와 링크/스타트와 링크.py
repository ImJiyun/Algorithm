import sys
input = sys.stdin.readline

N = int(input())

S = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
min_diff = float('inf')

def dfs(idx, cnt):
    global min_diff
    if cnt == N // 2:
        sum_a, sum_b = 0, 0
        for i in range(N):
            for j in range(i+1, N):
                if visited[i] and visited[j]:
                    sum_a += S[i][j] + S[j][i]
                elif not visited[i] and not visited[j]:   
                    sum_b += S[i][j] + S[j][i]
        min_diff = min(min_diff, abs(sum_a - sum_b))
        if min_diff == 0:
            print(0)
            sys.exit()
        return
    for i in range(idx, N):
        if visited[i]:
            continue
        visited[i] = True
        dfs(i + 1, cnt + 1)
        visited[i] = False
dfs(0, 0)
print(min_diff)