import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
X, Y, Z = map(int, input().split())    

def dijkstra(start, skipped):
    distance = [float('inf')] * (N+1)
    distance[start] = 0
    h = [(0, start)]
    
    while h:
        cur_dist, cur_node = heapq.heappop(h)
        
        if cur_dist > distance[cur_node]:
            continue
            
        for next_node, weight in graph[cur_node]:
            if skipped and next_node == Y:
                continue
            next_dist = cur_dist + weight    
            if next_dist < distance[next_node]:    
                distance[next_node] = next_dist
                heapq.heappush(h, (next_dist, next_node))
            
    return distance        
    
dist_from_x = dijkstra(X, False)
dist_from_y = dijkstra(Y, False)
dist_skip_y = dijkstra(X, True)

to_y = dist_from_x[Y]
y_to_z = dist_from_y[Z]
skip_to_z = dist_skip_y[Z]

first_value = to_y + y_to_z if to_y != float('inf') and y_to_z != float('inf') else -1
second_value = skip_to_z if skip_to_z != float('inf') else -1

print(first_value, second_value)