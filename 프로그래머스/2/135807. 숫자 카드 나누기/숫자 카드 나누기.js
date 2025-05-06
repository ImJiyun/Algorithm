function solution(arrayA, arrayB) {
    
    function findGcp(a, b) {
        while (b !== 0) {
            [a, b] = [b, a % b];
        }
        return a;
    }
    
    function gcp(array) {
        return array.reduce((acc, cur) => findGcp(acc, cur));
    }
    
    function isDivisible(target, arr) {
        return arr.some(num => num % target === 0);
    }
    
    const gcpA = gcp(arrayA);
    const gcpB = gcp(arrayB);
    
    let result = 0;
    
    if (!isDivisible(gcpA, arrayB)) result = gcpA;
    if (!isDivisible(gcpB, arrayA)) result = Math.max(result, gcpB);
    
    return result;
}