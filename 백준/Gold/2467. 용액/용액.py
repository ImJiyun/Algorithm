import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

nums.sort()
left, right, min_total = 0, N-1, float('inf')
ans = (0, 0)

while left < right:
    total = nums[left] + nums[right]
    if abs(total) < min_total:
        min_total = abs(total)
        ans = (nums[left], nums[right])
    if total > 0:
        right -= 1
    elif total < 0:
        left += 1
    else:
        break
print(f'{ans[0]} {ans[1]}')    