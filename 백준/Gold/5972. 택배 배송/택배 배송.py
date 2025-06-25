import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
    
dist = [float('inf')] * (N+1)  
dist[1] = 0

h = [(0, 1)]

while h:
    cur_dist, cur_node = heapq.heappop(h)
    
    if cur_dist > dist[cur_node]:
        continue
        
    for next_node, weight in graph[cur_node]:
        next_dist = cur_dist + weight
        if next_dist < dist[next_node]:
            dist[next_node] = next_dist
            heapq.heappush(h, (next_dist, next_node))
            
print(dist[N])            