function solution(number, k) {
    const stack = [];
    
    // [1]
    // [9]
    // [9, 2]
    // [9, 4]
    for (let i = 0; i < number.length; i++) {
        while (k > 0 && stack.length > 0 && stack[stack.length - 1] < number[i]) {
            stack.pop();
            k--;
        }
        stack.push(number[i]);
    }
    
    return stack.slice(0, number.length - k).join("");
}