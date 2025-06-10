import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

min_len = float('inf')
total = 0
start = 0

for end in range(N):
    total += nums[end]
    
    while total >= S:
        min_len = min(min_len, end-start+1)
        total -= nums[start]
        start += 1
        
if min_len == float('inf'):
    print(0)
else:
    print(min_len)