def solution(wallpaper):
    R, C = len(wallpaper), len(wallpaper[0])
    
    rows, cols = [0] * R, [0] * C
    
    for r in range(R):
        for c in range(C):
            if wallpaper[r][c] == '#':
                rows[r] += 1
    
    for c in range(C):
        for r in range(R):
            if wallpaper[r][c] == '#':
                cols[c] += 1
            
    rIdxs = [i for i, n in enumerate(rows) if n > 0]
    cIdxs = [i for i, n in enumerate(cols) if n > 0]
            
    return [rIdxs[0], cIdxs[0], rIdxs[-1] + 1, cIdxs[-1] + 1]