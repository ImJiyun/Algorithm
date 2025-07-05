import sys
input = sys.stdin.readline

N, M = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]
A = int(input())
col_sums = [0] * M

for c in range(M):
    for r in range(N):
        col_sums[c] += grid[r][c]
        
largest = sum(col_sums[:A])
total = largest

for i in range(A, M):
    total -= col_sums[i-A]
    total += col_sums[i]
    largest = max(largest, total)
    
print(largest)    