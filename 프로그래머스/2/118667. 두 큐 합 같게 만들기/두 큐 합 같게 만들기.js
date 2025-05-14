function solution(queue1, queue2) {
    
    // 3 2 7 2 4 6 5 1
    
    // 3 2 7 2 합 14
    // 4 6 5 1 합 16
    
    // 3 2 7 2 4 합 18
    // 6 5 1 합 12
    
    // 2 7 2 4 합 15
    // 6 5 1 3 합 15
    
    let sum1 = queue1.reduce((a, b) => a + b, 0);
    let sum2 = queue2.reduce((a, b) => a + b, 0);
    
    const q = [...queue1, ...queue2];
    const target = (sum1 + sum2) / 2;
    let cnt = 0;
    let leftIdx = 0;
    let rightIdx = queue1.length;
    
    while (cnt < queue1.length * 3) {
        if (sum1 === target) return cnt;
        else if (sum1 < target) {
            sum1 += q[rightIdx];
            rightIdx++;
        } else {
            sum1 -= q[leftIdx];
            leftIdx++
        }
        cnt++;
    }
    
    
//     while (queue1.length > 0 && queue2.length > 0) {
//         if (sum1 === sum2) return cnt;
//         else if (sum1 < sum2) {
//             const popped = queue2.shift(); // 이 부분 때문에 시간 초과 
//             queue1.push(popped);
//             sum1 += popped;
//             sum2 -= popped;
//             cnt++;
//         } else {
//             const popped = queue1.shift();
//             queue2.push(popped);
//             sum1 -= popped;
//             sum2 += popped;
//             cnt++;
//         }
        
//     }
    return -1;
}