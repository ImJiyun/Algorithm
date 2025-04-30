function solution(numbers) {
    const set = new Set();
    
    function isPrime(number) {
        if (number < 2) return false;
        for (let i = 2; i < number; i++) {
            if (number % i === 0) return false;
        }
        return true;
    }
    
    function getPermutations(arr, selectedNum, curr = "", used = Array(arr.length).fill(false)) {
        if (curr.length === selectedNum) {
            set.add(Number(curr));
            return;
        }
        
        for (let i = 0; i < arr.length; i++) {
            if (!used[i]) {
                used[i] = true;
                getPermutations(arr, selectedNum, curr + arr[i], used);
                used[i] = false;
            }
        }
    }
    
    const nums = numbers.split("");
    
    for (let len = 1; len <= numbers.length; len++) {
        getPermutations(nums, len);
    }
    
    let count = 0;
    for (const num of set) {
        if (isPrime(num)) count++
    }
    
    return count;
}