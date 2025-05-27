def solution(s):
    stack = []
    for item in s.split():
        if item == "Z":
            if stack:
                stack.pop()
        else:
            stack.append(int(item))
    return sum(stack)
