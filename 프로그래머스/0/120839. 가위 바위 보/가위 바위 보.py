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
    d = {
        "2" : "0",
        "0" : "5",
        "5" : "2"
    }
    # for choice in rsp:
    #     if choice == "2":
    #         answer += "0"
    #     elif choice == "0":
    #         answer += "5"
    #     else:
    #         answer += "2"
    
    
    return ''.join(d[choice] for choice in rsp)