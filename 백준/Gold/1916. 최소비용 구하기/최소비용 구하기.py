import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = defaultdict(list)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
start, end = map(int, input().split())
dists = [float('inf')] * (N + 1)
dists[start] = 0
h = [(start, 0)]

while h:
    cur_node, cur_dist = heapq.heappop(h)
    
    if cur_dist > dists[cur_node]:
        continue
    
    for next_node, cost in graph[cur_node]:
        if cost + cur_dist < dists[next_node]:
            dists[next_node] = cost + cur_dist
            heapq.heappush(h, (next_node, dists[next_node]))
      
print(dists[end])    