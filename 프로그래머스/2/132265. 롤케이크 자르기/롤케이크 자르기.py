from collections import defaultdict
def solution(topping):
    cnt = 0
    
    da = defaultdict(int)
    db = defaultdict(int)
    
    for i in range(len(topping)):
        if i == 0:
            da[topping[i]] += 1
        else:
            db[topping[i]] += 1
    
    for i in range(1, len(topping)-1):
        da[topping[i]] += 1
        
        db[topping[i]] -= 1
        if db[topping[i]] == 0:
            del db[topping[i]]
        
        if len(da) == len(db):
            cnt += 1
            
    return cnt