def solution(people, limit):
    cnt = 0
    lIdx = 0
    rIdx = len(people) - 1
    
    people.sort()
    
    while lIdx <= rIdx:
        if people[lIdx] + people[rIdx] <= limit:
            lIdx += 1
        rIdx -= 1
        cnt += 1
        
    return cnt