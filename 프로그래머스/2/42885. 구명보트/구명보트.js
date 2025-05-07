function solution(people, limit) {    
    people.sort((a, b) => a - b);
    let startIdx = 0;
    let lastIdx = people.length - 1;
    let boat = 0;

    // 30 50 50 70 100 [limit : 100]
    // [100]
    // [30, 70] lastIdx = N - 2
    // [50, 50] lastIdx = N - 3
    while (startIdx <= lastIdx) {
        if (people[startIdx] + people[lastIdx] <= limit) {
            startIdx++;
        }
        lastIdx--;
        boat++;
    }
    
    return boat;
}