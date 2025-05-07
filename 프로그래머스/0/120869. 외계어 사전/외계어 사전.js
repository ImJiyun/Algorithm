function solution(spell, dic) {
    const visited = Array(spell.length).fill(false);
    let found = false;
    
    function permute(arr) {
        if (arr.length === spell.length) {
            if (dic.includes(arr.join(""))) {
                found = true;
            }
            return;
        }
        
        for (let i = 0; i < spell.length; i++) {
            if (visited[i]) continue;
            visited[i] = true;
            arr.push(spell[i]);
            permute(arr);
            if (found) return;
            arr.pop();
            visited[i] = false;
        }

    }
    
    permute([]);
    
    return found ? 1 : 2;
}