import sys
input = sys.stdin.readline

N, K, B = map(int, input().split())
broken_lights = set(int(input()) for _ in range(B))

cnt = 0
for n in range(1, K+1):
    if n in broken_lights:
        cnt += 1
min_cnt = cnt

for i in range(2, N-K+2):
    if i-1 in broken_lights:
        cnt -= 1
    if i+K-1 in broken_lights:
        cnt += 1
    min_cnt = min(min_cnt, cnt)
    
print(min_cnt)    