function solution(wallpaper) {
    const R = wallpaper.length;
    const C = wallpaper[0].length;

    const rows = Array(R).fill(0);
    const cols = Array(C).fill(0);

    for (let r = 0; r < R; r++) {
        for (let c = 0; c < C; c++) {
            if (wallpaper[r][c] === '#') {
                rows[r]++;
                cols[c]++;
            }
        }
    }

    const strR = rows.findIndex(n => n > 0);
    const strC = cols.findIndex(n => n > 0);

    let endR = -1;
    for (let i = R - 1; i >= 0; i--) {
        if (rows[i] > 0) {
            endR = i;
            break;
        }
    }

    let endC = -1;
    for (let i = C - 1; i >= 0; i--) {
        if (cols[i] > 0) {
            endC = i;
            break;
        }
    }

    return [strR, strC, endR + 1, endC + 1];
}