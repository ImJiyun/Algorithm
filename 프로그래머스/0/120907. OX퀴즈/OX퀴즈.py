def solution(quiz):
    answer = []
    for item in quiz:
        # arr = item.split()
        # a, b, c = int(arr[0]), int(arr[2]), int(arr[4])
        # operator = arr[1]
        # if operator == '+':
        #     if a + b == c:
        #         answer.append('O')
        #     else:
        #         answer.append('X')
        # else:
        #     if a - b == c:
        #         answer.append('O')
        #     else:
        #         answer.append('X')
        a, op, b, _, c = item.split()
        a, b, c = int(a), int(b), int(c)
        
        if op == '+':
            answer.append('O' if a + b == c else 'X')
        else:
            answer.append('O' if a - b == c else 'X')
                
    return answer