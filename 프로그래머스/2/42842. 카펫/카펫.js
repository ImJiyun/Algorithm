function solution(brown, yellow) {
    const answer = [];
    
    const sum = (brown - 4) / 2;
    
    const mul = yellow;
    
    for (let i = 1; i < sum; i++) {
        if (i * (sum - i) === mul) {
            answer.push(i + 2);
            answer.push(sum - i + 2);
            break;
        }
    }
    
    return answer.sort((a,b) => b - a);
}