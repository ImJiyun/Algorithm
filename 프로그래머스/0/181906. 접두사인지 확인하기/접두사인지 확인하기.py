def solution(my_string, is_prefix):
    # for i in range(len(my_string)):
    #     if (is_prefix == my_string[:i]):
    #         return 1
    # return 0
    return int(my_string.startswith(is_prefix))