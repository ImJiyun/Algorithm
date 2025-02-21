function solution(arr) {
    var answer = [];

    for (let item of arr) {
        if (answer.length === 0 || answer[answer.length - 1] !== item) {
            answer.push(item);
        }
    }

    return answer;
}
