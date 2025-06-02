def solution(numbers):
    strs = list(map(str, numbers))
    # '3333333333' > '30303030303030303030'
    strs.sort(key=lambda x:x*10, reverse=True)
    return ''.join(strs) if int(strs[0]) != 0 else '0'