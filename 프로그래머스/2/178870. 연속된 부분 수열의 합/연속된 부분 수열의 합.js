function solution(sequence, k) {
    let left = 0;
    let right = 0;
    let sum = sequence[0];
    let answer = [];

    while (right < sequence.length) {
        if (sum === k) {
            answer.push([left, right]);
            sum -= sequence[left];
            left++;
        } else if (sum < k) {
            right++;
            if (right < sequence.length) sum += sequence[right];
        } else { 
            sum -= sequence[left];
            left++;
        }
    }

    answer.sort((a, b) => {
        const lenA = a[1] - a[0];
        const lenB = b[1] - b[0];
        if (lenA === lenB) return a[0] - b[0];
        return lenA - lenB;
    });

    return answer[0];
}