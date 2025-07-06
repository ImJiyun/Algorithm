import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
intervals = [list(map(int, input().split())) for _ in range(M)]

prefix_sum = [[0] * (N+1) for _ in range(N+1)]

for r in range(1, N+1):
    for c in range(1, N+1):
        prefix_sum[r][c] = (
            prefix_sum[r-1][c] +
            prefix_sum[r][c-1] -
            prefix_sum[r-1][c-1] +
            table[r-1][c-1]
        )
        
for x1, y1, x2, y2 in intervals:
    total = prefix_sum[x2][y2] - prefix_sum[x2][y1-1] - prefix_sum[x1-1][y2] + prefix_sum[x1-1][y1-1]
    print(total)    