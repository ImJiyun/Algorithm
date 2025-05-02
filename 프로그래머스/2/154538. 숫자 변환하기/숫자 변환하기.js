function solution(x, y, n) {
    let currentSet = new Set([x]);
    let visited = new Set([x]);
    let count = 0;

    while (currentSet.size > 0) {
        const nextSet = new Set();
        count++;

        for (let value of currentSet) {
            for (let next of [value + n, value * 2, value * 3]) {
                if (next === y) return count;
                if (next < y && !visited.has(next)) {
                    visited.add(next);
                    nextSet.add(next);
                }
            }
        }

        currentSet = nextSet;
    }

    return x === y ? 0 : -1;
}