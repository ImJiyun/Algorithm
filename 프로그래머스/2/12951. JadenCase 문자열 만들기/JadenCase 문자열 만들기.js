function solution(s) {
    const words = s.split(" ");
    let idx = 0;
    
    for (let word of words) {
        if (word === "") {
            idx++;
            continue; 
        }
        let first;
        if (!isNaN(word[0])) {
            first = word[0];
        } else {
            first = word[0].toUpperCase();
        }
        words[idx] = first.concat(word.slice(1).toLowerCase());
        idx++;
    }
    return words.join(" ");
}