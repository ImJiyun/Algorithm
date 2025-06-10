import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()

left, right = 0, n - 1

cnt = 0

# while left <= n-2:
#     right = left + 1
#     while right <= n-1:
#         if nums[left] + nums[right] == x:
#             cnt += 1
#         right += 1
#     left += 1   

while left < right:
    total = nums[left] + nums[right]
    if total >= x:
        if total == x:
            cnt += 1
        right -= 1
    elif total < x:
        left += 1
        
print(cnt)