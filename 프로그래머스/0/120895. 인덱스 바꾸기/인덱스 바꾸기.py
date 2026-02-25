def solution(my_string, num1, num2):
    a, b = my_string.index(num1), my_string.index(num2)
    my_string[num1], my_string = a, b
    return a, b