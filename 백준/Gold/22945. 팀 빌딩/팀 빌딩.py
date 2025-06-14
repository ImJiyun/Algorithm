import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
left, right = 0, N-1
max_skill = 0

while left < right:
    skill = (right-left-1) * min(nums[left], nums[right])
    if skill > max_skill:
        max_skill = skill
        
    if nums[left] < nums[right]:
        left += 1
    else:
        right -= 1

print(max_skill)        