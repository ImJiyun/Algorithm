import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = defaultdict(list)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
dist = [float('inf')] * (V+1)
dist[K] = 0
h = [(0, K)]    

while h:
    cur_dist, cur_node = heapq.heappop(h)
    
    if cur_dist > dist[cur_node]:
        continue
    
    for next_node, cost in graph[cur_node]:
        if cur_dist + cost < dist[next_node]:
            dist[next_node] = cur_dist + cost
            heapq.heappush(h, (dist[next_node], next_node))
            
for i in range(1, V+1):
    if dist[i] == float('inf'):
        print('INF')
    else:
        print(dist[i])