# def solution(rsp):
#     answer = ''
#     for choice in rsp:
#         if choice == "2":
#             answer.join("0")
#         elif choice == "0":
#             answer.join("5")
#         else:
#             answer.join("2")
#     return answer

def solution(rsp):
    answer = ''
    for choice in rsp:
        if choice == "2":
            answer += "0"
        elif choice == "0":
            answer += "5"
        else:
            answer += "2"
    return answer