function solution(triangle) {
    let prev = [triangle[0][0]];

    for (let i = 1; i < triangle.length; i++) {
        const row = triangle[i];
        const curr = [];

        curr[0] = prev[0] + row[0];  // 맨 왼쪽

        for (let j = 1; j < row.length - 1; j++) {
            curr[j] = Math.max(prev[j - 1], prev[j]) + row[j];
        }

        curr[row.length - 1] = prev[prev.length - 1] + row[row.length - 1];  // 맨 오른쪽

        prev = curr;  // 다음 단계에 사용할 줄 업데이트
    }

    return Math.max(...prev);
}
