def solution(arr):
    return [
        num / 2 if num % 2 == 0 and num >= 50 
        else num * 2 if num % 2 == 1 and num < 50
        else num
        for num in arr
    ]