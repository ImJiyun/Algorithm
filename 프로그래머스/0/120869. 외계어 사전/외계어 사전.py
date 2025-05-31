def solution(spell, dic):
    arr = []
    found = [False]
    visited = [False] * len(spell)
    
    def permute():
        if len(arr) == len(spell):
            word = ''.join(arr)
            if word in dic:
                found[0] = True
            return
        for i in range(len(spell)):
            if visited[i]:
                continue
            arr.append(spell[i])
            visited[i] = True
            permute()
            arr.pop()
            visited[i] = False
            
    permute()         
    return 1 if found[0] else 2