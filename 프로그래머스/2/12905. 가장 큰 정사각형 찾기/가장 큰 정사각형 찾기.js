function solution(board) {
    
    let max = 0;
    
    for (let r = 1; r < board.length; r++) {
        for (let c = 1; c < board[0].length; c++) {
            if (board[r][c] === 1) {
                board[r][c] = Math.min(board[r-1][c-1], board[r-1][c], board[r][c-1]) + 1;
            }
            max = Math.max(max, board[r][c]);
        }
    }
    
    if (max === 0 && board.flat().includes(1)) return 1
    
    return max * max;
}