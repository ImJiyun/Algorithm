def solution(players, callings):
    orders = {player: idx for idx, player in enumerate(players)}
    
    for calling in callings:
        current_order = orders[calling]
        front_order = current_order - 1
        
        front_player = players[front_order] 
        
        orders[calling] -= 1
        orders[front_player] += 1
        
        players[front_order], players[current_order] = players[current_order], players[front_order]
        
        
    return players