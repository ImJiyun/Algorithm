import sys
input = sys.stdin.readline

K, N = map(int, input().split())

lines = [int(input()) for _ in range(K)]
left, right = 1, max(lines)
answer = 0

while left <= right:
    mid = (left+right) // 2
    cut = sum(line // mid for line in lines)
    if cut >= N:         
        answer = mid     
        left = mid + 1   
    else:
        right = mid - 1
print(right)        