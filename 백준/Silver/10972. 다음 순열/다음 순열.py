import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

i = len(arr) - 2
    
while i >= 0 and arr[i] > arr[i+1]:
    i -= 1
if i == -1:
    print(-1)
    sys.exit(0)

j = len(arr) -1
while j >= 0 and arr[i] > arr[j]:
    j -= 1
    
arr[i], arr[j] = arr[j], arr[i]

arr[i+1:] = reversed(arr[i+1:])

print(' '.join(map(str, arr)))