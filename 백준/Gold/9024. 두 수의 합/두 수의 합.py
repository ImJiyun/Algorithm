import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    
    nums.sort()
    
    left, right = 0, n-1
    diff = float('inf')
    cnt = 0
    
    while left < right:
        total = nums[left] + nums[right]
        new_diff = abs(k - total)
        if diff > new_diff:
            cnt = 1
        elif diff == new_diff:
            cnt += 1
        diff = min(diff, new_diff)   
        
        if total == k:
            left += 1
            right -= 1
        elif total < k:
            left += 1
        elif total > k:
            right -= 1
    
    print(cnt)