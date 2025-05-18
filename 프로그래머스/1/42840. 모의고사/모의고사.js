function solution(answers) {
    const ans1 = [1, 2, 3, 4, 5];
    const ans2 = [2, 1, 2, 3, 2, 4, 2, 5];
    const ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    
    let cnt1 = 0, cnt2 = 0, cnt3 = 0;
    
    for (let i = 0; i < answers.length; i++) {
        if (ans1[i % ans1.length] === answers[i]) cnt1++;
        if (ans2[i % ans2.length] === answers[i]) cnt2++;
        if (ans3[i % ans3.length] === answers[i]) cnt3++;
    }
    
    const arr = [[1, cnt1], [2, cnt2], [3, cnt3]];
    arr.sort((a, b) => b[1] - a[1]);
    
    const answer = [arr[0][0]];
    for (let i = 1; i < arr.length; i++) {
        if (arr[i][1] < arr[0][1]) break;
        answer.push(arr[i][0]);
    }
    
    return answer;
}