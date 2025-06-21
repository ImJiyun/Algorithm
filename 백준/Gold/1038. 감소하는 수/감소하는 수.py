import sys
input = sys.stdin.readline

N = int(input())

result = []

def dfs(n, last_digit):
    result.append(n)
        
    for next_digit in range(0, last_digit):
        dfs(n * 10 + next_digit, next_digit)
        
for i in range(10):
    dfs(i, i)

result.sort()

if N >= len(result):
    print(-1)
else:
    print(result[N])