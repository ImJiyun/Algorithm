import sys, heapq
input = sys.stdin.readline


n, d = map(int, input().split())

graph = [[] for _ in range(d+1)]

for i in range(d):
    graph[i].append((i+1, 1))
    
for _ in range(n):
    start, end, cost = map(int, input().split())
    if end > d:
        continue
    if cost < end - start:
        graph[start].append((end, cost))
        
distance = [float('inf')] * (d+1)
distance[0] = 0
heap = [(0, 0)]

while heap:
    dist, now = heapq.heappop(heap)
    
    if distance[now] < dist:
        continue
    
    for next_node, weight in graph[now]:
        if distance[next_node] > dist + weight:
            distance[next_node] = dist + weight
            heapq.heappush(heap, (distance[next_node], next_node))
          
print(distance[d])        