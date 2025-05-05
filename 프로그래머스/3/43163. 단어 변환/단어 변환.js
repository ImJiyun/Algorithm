function solution(begin, target, words) {
    if (!words.includes(target)) return 0;

    function isConnected(word1, word2) {
        let diff = 0;
        for (let i = 0; i < word1.length; i++) {
            if (word1[i] !== word2[i]) diff++;
            if (diff > 1) return false;
        }
        return diff === 1;
    }

    let min = Infinity;
    
    function dfs(current, count, visited) {
        if (current === target) {
            min = Math.min(min, count);
            return;
        }
        for (let i = 0; i < words.length; i++) {
            if (!visited[i] && isConnected(current, words[i])) {
                visited[i] = true;
                dfs(words[i], count + 1, visited);
                visited[i] = false;
            }
        }
    }

    dfs(begin, 0, Array(words.length).fill(false));
    return min === Infinity ? 0 : min;
}