def solution(begin, target, words):
    
    if target not in words:
        return 0

    N = len(words)
    visited = [False] * N
    
    def diff(word1, word2):
        count = 0
        for i in range(N):
            if word1[i: i+1] != word2[i: i+1]:
                count += 1
        return count == 1
    
    count = [0]
    
    def dfs(word, cnt):
        if (word == target):
            count[0] = cnt
            return
        
        for i in range(N):
            if not visited[i] and diff(word, words[i]):
                visited[i] = True
                dfs(words[i], cnt + 1)
                visited[i] = False
    
    dfs(begin, 0)
    
    return count[0]