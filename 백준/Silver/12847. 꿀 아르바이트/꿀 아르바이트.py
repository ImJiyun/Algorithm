import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sals = list(map(int, input().split()))

left, right = 0, m-1

profit = sum([sals[i] for i in range(left, right+1)])
max_profit = profit

while right + 1 < n:
    profit -= sals[left]
    left += 1
    right += 1
    profit += sals[right]
    max_profit = max(max_profit, profit)
    
print(max_profit)