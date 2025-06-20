import sys
input = sys.stdin.readline

L, C = map(int, input().split())
alphabets = list(input().split())
alphabets.sort()

arr = []
visited = [False] * C

def dfs(idx):
    if len(arr) == L:
        cnt = 0
        for char in arr:
            if char in 'aeiou':
                cnt += 1
        if cnt >= 1 and L-cnt >= 2:
            print(''.join(arr))
        return
    for i in range(idx, C):
        if visited[i]:
            continue
        visited[i] = True
        arr.append(alphabets[i])
        dfs(i+1)
        arr.pop()
        visited[i] = False
dfs(0)        