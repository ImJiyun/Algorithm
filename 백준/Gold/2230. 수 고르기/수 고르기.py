import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [0] * N
for i in range(N):
    nums[i] = int(input())

nums.sort()
left, right = 0, 1
min_diff = float('inf')

while right < N:
    diff = nums[right] - nums[left]
    if diff >= M and left < right:
        min_diff = min(min_diff, diff)
        left += 1
        continue
    right += 1
print(min_diff)    