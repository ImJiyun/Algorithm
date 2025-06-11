import sys
input = sys.stdin.readline

N, X = map(int, input().split())
nums = list(map(int, input().split()))
left, right = 0, X-1
max_total = sum([nums[i] for i in range(X)])
total = max_total
cnt = 1

while right + 1 < N:
    total -= nums[left]
    left += 1
    right += 1
    total += nums[right]
    if max_total < total:
        cnt = 1
        max_total = total
    elif max_total == total:
        cnt += 1
        
if max_total > 0:
    print(max_total)
    print(cnt)
else:
    print('SAD')