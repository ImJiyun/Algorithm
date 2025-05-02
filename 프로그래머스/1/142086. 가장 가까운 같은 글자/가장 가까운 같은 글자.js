function solution(s) {
    const answer = [];
    const strs = s.split("");
    const visited = new Set();
    
    for (let idx = 0; idx < strs.length; idx++) {
        if (!visited.has(strs[idx])) {
            answer.push(-1);
            visited.add(strs[idx]);
        }
        else {
            let dist = 1;
            while (strs[idx-dist] !== strs[idx]) {
                dist++;
            }
            answer.push(dist);
        }
    }
    return answer;
}