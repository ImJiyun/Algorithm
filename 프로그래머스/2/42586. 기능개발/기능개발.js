function solution(progresses, speeds) {
    const answer = [];
    
    const remaining = [];
    for (let i = 0; i < progresses.length; i++) {
        remaining.push(Math.ceil((100 - progresses[i]) / speeds[i]))
    }
    
    while (remaining.length > 0) {
        let count = 1;
        const popped = remaining.shift();
     
        while (remaining[0] <= popped) {
            remaining.shift();
            count++;
        }
        answer.push(count);
    }
    return answer;
}