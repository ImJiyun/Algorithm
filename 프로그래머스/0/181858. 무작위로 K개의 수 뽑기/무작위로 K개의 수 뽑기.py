def solution(arr, k):
    result = []
    seen = set()
    
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
            if len(result) == k:
                break
                
    while len(result) < k:
        result.append(-1)

    return result