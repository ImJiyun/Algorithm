import heapq
def solution(scoville, K):
    pq = scoville
    heapq.heapify(pq)
    cnt = 0
    
    while pq and pq[0] < K:
        if len(pq) < 2:
            return -1
        first = heapq.heappop(pq)
        second = heapq.heappop(pq)
        heapq.heappush(pq, first + second * 2)
        cnt += 1
        
    return cnt