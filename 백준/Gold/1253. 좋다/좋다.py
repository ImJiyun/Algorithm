import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
cnt = 0

A.sort()

for i in range(N):
    left, right = 0, N-1
    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue
            
        if A[left] + A[right] == A[i]:
            cnt += 1
            break
        elif A[left] + A[right] > A[i]:
            right -= 1
        else:
            left += 1
print(cnt)            