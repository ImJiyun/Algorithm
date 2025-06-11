import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dolls = list(map(int, input().split()))

left, right, cnt = 0, 0, 0
min_length = float('inf')

while right < N:
    if dolls[right] == 1:
        cnt += 1
    while cnt == K:
        min_length = min(min_length, right-left+1)
        if dolls[left] == 1:
            cnt -= 1
        left += 1
    right += 1
print(min_length if min_length != float('inf') else -1)