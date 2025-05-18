function solution(s) {
    const str = s.split(" ");
    const sorted = str.sort((a, b) => Number(a) - Number(b));
    let min = sorted[0];
    let max = sorted[sorted.length - 1];
    return `${min} ${max}`;
}