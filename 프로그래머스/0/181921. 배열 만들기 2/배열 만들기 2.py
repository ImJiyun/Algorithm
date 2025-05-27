def solution(l, r):
    answer = []
    nums = ["5", "0"]
    
    def dfs(n):
        val = int(n)
        if val > r:
            return
        if val >= l:
            answer.append(val)
        
        for nxt in nums:
            dfs(n + nxt)

    dfs("5")
    
    return sorted(answer) if answer else [-1]