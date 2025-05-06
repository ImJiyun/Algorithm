function solution(n, lost, reserve) {
    const realLost = lost.filter(l => !reserve.includes(l)).sort((a, b) => a - b);
    const realRes = reserve.filter(r => !lost.includes(r)).sort((a, b) => a - b);
    
    for (let r of realRes) {
        // 앞 번호
        const frontIdx = realLost.indexOf(r - 1);
        if (frontIdx !== -1) {
            realLost.splice(frontIdx, 1);
            continue;
        }
        
        // 뒷 번호
        const afterIdx = realLost.indexOf(r + 1);
        if (afterIdx !== -1) {
            realLost.splice(afterIdx, 1);
        }
    }
    return n - realLost.length;
}