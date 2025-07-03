import sys
from collections import defaultdict
input = sys.stdin.readline

def make_palindrom(s):
    cnt = defaultdict(int)
    odd_cnt = 0
    odd_chr = ''
    
    for ch in s:
        cnt[ch] += 1
        
    for ch in cnt:
        if cnt[ch] % 2 == 1:
            odd_cnt += 1
            odd_chr = ch
        
    if odd_cnt > 1:
        return "I'm Sorry Hansoo"
    
    l = len(s)
    substr = ''
    if l % 2 == 0:
        for ch in sorted(cnt):
            substr += ch * (cnt[ch] // 2)
        return substr + substr[::-1]    
    else:    
        for ch in sorted(cnt):
            substr += ch * (cnt[ch] // 2)
        return substr + odd_chr +  substr[::-1]  
    
s = input().strip()
ans = make_palindrom(s)
print(ans)