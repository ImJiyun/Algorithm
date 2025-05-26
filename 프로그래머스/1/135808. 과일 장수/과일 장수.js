function solution(k, m, score) {
    // 3 3 2 2 1 1 1
    score.sort((a, b) => b - a);
    
    let answer = 0;
    
    for (let i = 0; i < score.length; i+=m) {
        if (score.length - i < m) break;
        const arr = score.slice(i, i+m);
        answer += score[i+m-1] * m;
    }
    
    return answer;
}