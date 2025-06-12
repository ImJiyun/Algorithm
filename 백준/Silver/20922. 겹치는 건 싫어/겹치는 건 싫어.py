import sys
from collections import defaultdict
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

left, right, max_length = 0, 0, 1
cnts = defaultdict(int)

while right < N:
    while cnts[nums[right]] >= K:
        cnts[nums[left]] -= 1
        left += 1    
    max_length = max(max_length, right-left+1)    
    cnts[nums[right]] += 1
    right += 1
    
print(max_length)