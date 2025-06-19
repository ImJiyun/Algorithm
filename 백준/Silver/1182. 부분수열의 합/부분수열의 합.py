import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0

def dfs(total, idx):
    global cnt
    
    if idx == N:
        if total == S:
            cnt += 1
        return
    
    dfs(total + nums[idx], idx+1)
    dfs(total, idx+1)

dfs(0, 0)
print(cnt if S != 0 else cnt - 1)