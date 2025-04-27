function solution(numbers) {
    const strs = numbers.map(num => num.toString());
    
    strs.sort((a, b) => (b + a) - (a + b));
    
    const answer = strs.join("");
    
    return answer[0] === "0" ? "0" : answer;
}