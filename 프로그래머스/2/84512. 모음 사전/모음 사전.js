function solution(word) {
    const alphabets = ['A', 'E', 'I', 'O', 'U'];
    let count = 0;
    let answer = 0;
    
    function dfs(str) {
        if (str === word) {
            answer = count;
            return;
        }
        if (str.length === 5) return;
        
        for (let i = 0; i < 5; i++) {
            count++;
            dfs(str + alphabets[i]);
            if (answer) return;
        }
    }
    
    dfs("");
    
    return answer;
}