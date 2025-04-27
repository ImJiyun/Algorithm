function solution(k, tangerine) {
    let answer = 0;
    const map = new Map();
    
    for (let item of tangerine) {
        map.set(item, map.has(item) ? map.get(item) + 1 : 1);
    }
    
    const counts = Array.from(map.values()).sort((a, b) => b - a);

    for (let count of counts) {
        k -= count;
        answer++;
        if (k <= 0) break;
    }
    
    return answer;
}
