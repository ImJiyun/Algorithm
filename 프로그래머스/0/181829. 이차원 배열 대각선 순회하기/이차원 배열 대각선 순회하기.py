def solution(board, k):
    # answer = 0
    # for r in range(len(board)):
    #     for c in range(len(board[r])):
    #         if board[r][c] <= k:
    #             answer += board[r][c]
    # return answer
    return sum(cell for r, row in enumerate(board) for c, cell in enumerate(row) if r + c <= k)