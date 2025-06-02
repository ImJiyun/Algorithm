def solution(numbers):
    cnt = 0
    nums = set()
    
    def dfs(l):
        if len(arr) == l:
            nums.add(int(''.join(arr)))
            return
        
        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                arr.append(numbers[i:i+1])
                dfs(l)
                arr.pop()
                visited[i] = False
                
    for length in range(1, len(numbers) + 1):
        visited = [False] * len(numbers)
        arr = []
        dfs(length)
        
    max_value = max(nums)
    is_prime = [True] * (max_value + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(max_value ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, max_value + 1, i):
                is_prime[j] = False
                
    for n in nums:
        if is_prime[n]:
            cnt += 1
        
    return cnt