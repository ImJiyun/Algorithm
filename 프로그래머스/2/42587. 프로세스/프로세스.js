function solution(priorities, location) {
    let order = 0;
    const queue = [];
    
    // original index, priority
    for (let i = 0; i < priorities.length; i++) {
        queue.push([i, priorities[i]]);
    }
    
    function findMax() {
        let max = -Infinity;
        for (let [idx, pri] of queue) {
            if (max < pri) max = pri;
        }
        return max;
    }
    
    while (queue.length > 0) {
        const curr = queue.shift();
        const max = findMax();
        if (curr[1] < max) queue.push(curr);
        else {
            order++;
            if (curr[0] === location) return order;
        }
    }
}