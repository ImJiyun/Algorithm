import sys
input = sys.stdin.readline

board = [list(map(int, input().strip().split())) for _ in range(19)]

dx = [0, 1, 1, -1]  
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        if board[x][y] == 0:
            continue
        player = board[x][y]
        for k in range(4):
            cnt = 1
            nx = x + dx[k]
            ny = y + dy[k]
            
            while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == player:
                cnt += 1
                if cnt > 5:  
                    break
                nx += dx[k]
                ny += dy[k]
            
            if cnt == 5:
                px = x - dx[k]
                py = y - dy[k]
                if 0 <= px < 19 and 0 <= py < 19 and board[px][py] == player:
                    continue
                
                if 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == player:
                    continue
                
                print(player)
                print(x + 1, y + 1)
                sys.exit()
print(0)                