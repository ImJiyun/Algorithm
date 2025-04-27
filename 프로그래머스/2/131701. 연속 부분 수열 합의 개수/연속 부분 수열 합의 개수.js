function solution(elements) {
    const set = new Set();
    const length = elements.length;
    const doubled = [...elements, ...elements];
    
    for (let len = 1; len <= length; len++) { 
        for (let i = 0; i < length; i++) {    
            let sum = 0;
            for (let j = i; j < i + len; j++) {
                sum += doubled[j];
            }
            set.add(sum);
        }
    }
    return set.size;
}
