import sys
input = sys.stdin.readline

N, D = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda item:item[0])

left, right, total, max_total = 0, 0, 0, 0

while right < N:
    total += arr[right][1]
    while arr[right][0] - arr[left][0] >= D:
        total -= arr[left][1]
        left += 1
    max_total = max(max_total, total)    
    right += 1
print(max_total)    