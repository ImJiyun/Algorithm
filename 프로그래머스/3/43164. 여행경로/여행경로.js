function solution(tickets) {
    const answer = [];
    const visited = new Set();
    
    const list = new Map();
    
    function putList(tickets) {
        for (let [src, dst] of tickets) {
            if (!list.has(src)) list.set(src, []);
            list.get(src).push(dst);
            list.get(src).sort();
        }
    }
    
    putList(tickets);
    
    function traverse(src) {
         while (list.has(src) && list.get(src).length > 0) {
            let dst = list.get(src).shift();
            traverse(dst);
        }
        answer.unshift(src);
    }
    
    traverse("ICN");
    
    return answer;
}