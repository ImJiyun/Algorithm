import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
k = int(input())

left, right, total, cnt = 0, 0, 0, 0

while right < n:
    total += nums[right]
    while total > k:
        cnt += (n-right)
        total -= nums[left]
        left += 1
    right += 1    
print(cnt)