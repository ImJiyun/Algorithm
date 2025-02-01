function solution(num_list, n) {
    for (let turn = 1; turn <= n; turn++) {
        let item = num_list.shift();
        num_list.push(item);
    }
    return num_list;
}