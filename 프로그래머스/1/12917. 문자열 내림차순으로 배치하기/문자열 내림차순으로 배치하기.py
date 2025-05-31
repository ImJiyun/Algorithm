def solution(s):
    
#     arr = list(s)
#     arr.sort( key=lambda x: -ord(x))
    
#     return ''.join(arr)
    return ''.join(sorted(s, reverse=True))