import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temps = list(map(int, input().split()))

prefix_sum = [0] * (N+1)

for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + temps[i-1]
    
max_total = float('-inf')    
for i in range(K, N+1):
    total = prefix_sum[i] - prefix_sum[i-K]
    max_total = max(max_total, total)
    
print(max_total)    