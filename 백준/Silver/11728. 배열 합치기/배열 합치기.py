import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = []
a, b = 0, 0

while a < N and b < M:
    if A[a] < B[b]:
        ans.append(A[a])
        a += 1
    else:
        ans.append(B[b])
        b += 1
    
if a < N:
    ans.extend(A[a:])

if b < M:
    ans.extend(B[b:])
   
print(' '.join(map(str, ans)))