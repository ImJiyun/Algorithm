import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    pairs = [tuple(map(int, input().split())) for _ in range(N)]
        
    pairs.sort(key=lambda x:x[0])
    cnt = 1
    min_second = pairs[0][1]
    
    for i in range(1, N):
        if pairs[i][1] < min_second:
            cnt += 1
            min_second = pairs[i][1]
            
    print(cnt)        