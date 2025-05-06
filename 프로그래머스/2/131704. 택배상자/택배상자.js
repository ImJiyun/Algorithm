function solution(order) {
    let curr = 1;
    const temp = [];
    const truck = [];

    for (let i = 0; i < order.length; i++) {
        const target = order[i];

        while (curr <= order.length && curr < target) {
            temp.push(curr);
            curr++;
        }

        if (curr === target) {
            truck.push(curr);
            curr++;
        } else if (temp[temp.length - 1] === target) {
            truck.push(temp.pop());
        } else {
            break;
        }
    }

    return truck.length;
}