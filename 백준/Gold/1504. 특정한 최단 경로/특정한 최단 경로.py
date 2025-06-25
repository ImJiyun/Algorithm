import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

N, E = map(int, input().split())

graph = defaultdict(list)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
    
v1, v2 = map(int, input().split())

def dijkstra(start):
    dist = [float('inf')] * (N+1)
    dist[start] = 0
    hp = [(0, start)]
    
    while hp:
        cost, node = heapq.heappop(hp)
        if cost > dist[node]:
            continue
        for next_node, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(hp, (new_cost, next_node))
    return dist

dist_from_1 = dijkstra(1)
dist_from_v1 = dijkstra(v1)
dist_from_v2 = dijkstra(v2)

route1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]
route2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]
                
result = min(route1, route2)

print(result if result < float('inf') else -1)