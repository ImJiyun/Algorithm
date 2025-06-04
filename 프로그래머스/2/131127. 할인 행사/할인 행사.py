from collections import defaultdict

def solution(want, number, discount):
    ans = 0
    
    d = {}
    for i in range(len(want)):
        d[want[i]] = number[i]
        
    for i in range(len(discount)  - 9):
        c = defaultdict(int)
        for j in range(i, i + 10):
            c[discount[j]] += 1
        
        matched = True
        for fruit in d:
            if d[fruit] != c[fruit]:
                matched = False
                break
    
        if matched:
            ans += 1
        
    return ans