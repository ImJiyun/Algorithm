function solution(numbers) {
    let sum = 0;
    
    for (let num of numbers) {
        sum += num;
    }
    return 45 - sum;
}