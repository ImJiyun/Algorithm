import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
intervals = [list(map(int, input().split())) for _ in range(M)]

prefix_sum = [0] * (N+1)

for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + A[i-1]
    
for a, b in intervals:
    print(prefix_sum[b] - prefix_sum[a-1])