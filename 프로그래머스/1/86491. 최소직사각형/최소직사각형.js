function solution(sizes) {
    let maxWidth = 0;
    let maxHeight = 0;
    
    for (let [w, h] of sizes) {
        let width = Math.max(w, h);
        let height = Math.min(w, h);
        
        maxWidth = Math.max(maxWidth, width);
        maxHeight = Math.max(maxHeight, height);
    }
    return maxWidth * maxHeight;
}