import sys
input = sys.stdin.readline

H, W = map(int, input().split())
ground = list(map(int, input().split()))

left_floor_max = [0] * W
right_floor_max = [0] * W

left_floor_max[0] = ground[0]
for i in range(1, W):
    left_floor_max[i] = max(ground[i], left_floor_max[i-1])

right_floor_max[-1] = ground[-1]
for i in range(W-2, -1, -1):
    right_floor_max[i] = max(ground[i], right_floor_max[i+1])
    
rain = 0    
for i in range(W):
    water = min(left_floor_max[i], right_floor_max[i]) - ground[i]
    if water > 0:
        rain += water
print(rain)    