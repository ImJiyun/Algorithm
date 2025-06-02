def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    ans = [0]
    cnt = [0]
    
    def dfs(str):
        if str == word:
            ans[0] = cnt[0]
            return
        
        if len(str) == 5:
            return
        
        for i, vowel in enumerate(vowels):
            cnt[0] += 1
            dfs(str + vowels[i])
            if ans[0]:
                return
            
    dfs('')
    
    return ans[0]