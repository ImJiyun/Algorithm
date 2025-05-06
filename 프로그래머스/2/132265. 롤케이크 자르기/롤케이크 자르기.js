function solution(topping) {
    let answer = 0;
    const left = new Map();
    const right = new Map();
    
    for (let item of topping) {
        if (!right.has(item)) right.set(item, 0);
        right.set(item, right.get(item) + 1);
    }
    
    for (let i = 0; i < topping.length; i++) {
        if (!left.has(topping[i])) left.set(topping[i], 0);
        left.set(topping[i], left.get(topping[i]) + 1);
        if (right.has(topping[i])) {
            right.set(topping[i], right.get(topping[i]) - 1);
            if (right.get(topping[i]) === 0) right.delete(topping[i]);
        }
        if (left.size === right.size) answer++;
    }
    
    return answer;
}