function solution(num, total) {
    let sum = 0; 
    for (let i = 1; i < num; i++) {
        sum += i;
    }
    let startPoint = (total - sum) / num;
    
    const answer = [];
    for (let i = 1; i <= num; i++) {
        answer.push(startPoint++);
    }
    return answer;
}