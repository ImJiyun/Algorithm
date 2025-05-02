function solution(prices) {
    const answer = [];
    let front = 0; 

    while (front < prices.length) {
        let dist = 0;
        for (let i = front + 1; i < prices.length; i++) {
            dist++;
            if (prices[front] > prices[i]) break;
        }
        answer.push(dist);
        front++;
    }

    return answer;
}