def solution(sequence):
    N = len(sequence)
    arr1 = [sequence[i] * 1 if i % 2 == 0 else sequence[i] * -1 for i in range(N)]
    arr2 = [sequence[i] * -1 if i % 2 == 0 else sequence[i] * 1 for i in range(N)]
    
    def sum_arr(arr):
        max_sum = curr_sum = arr[0]
        
        for num in arr[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
            
        return max_sum
    
    return max(sum_arr(arr1), sum_arr(arr2))