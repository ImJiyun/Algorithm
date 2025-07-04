import heapq

def solution(operations):
    pq = []
    for op in operations:
        alphabet, str_num = op.split()
        num = int(str_num)
        
        if alphabet == 'I':
            heapq.heappush(pq, num)
        elif pq and alphabet == 'D':
            if num == -1:
                heapq.heappop(pq)
            else:
                pq.remove(max(pq))
                heapq.heapify(pq)

    return [max(pq), min(pq)] if pq else [0, 0]