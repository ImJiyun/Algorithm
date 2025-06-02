def solution(arr1, arr2):
    # arr1[0][0] + arr2[0][0], arr1[0][1] + arr2[0][1]
    # arr1[1][0] + arr2[1][0], arr2[1][1] + arr2[1][1]
    answer = []
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr1[0])):
            row.append(arr1[i][j] + arr2[i][j])
        answer.append(row)
    return answer