function solution(citations) {
    let curr = 1;
    let hIdx = 0;
    citations.sort((a, b) => b - a);
    
    for (let citation of citations) {
        if (citation >= curr) hIdx = Math.max(hIdx, curr);
        else break;
        curr++;
    }
    return hIdx;
}