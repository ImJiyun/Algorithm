function solution(name) {
    let answer = 0;
    const len = name.length;
    // 알파벳 교체 횟수 구하기
    for (let i = 0; i < len; i++) {
        const charCode = name.charCodeAt(i);
        answer += Math.min(charCode - 65, 91 - charCode);
    }
    
    // 커서 움직임 구하기
    // JJJAAAAAJ (length : 9)
    let move = len - 1;
    for (let i = 0; i < len; i++) {
        let next = i + 1;
        while (next < len && name[next] === "A") next++;
        
        move = Math.min(move, i + len - next + Math.min(i, len - next));    
    }
    return answer + move;
}