def solution(s):
    nums = sorted(list(map(int, s.split())))
    return str(nums[0]) + ' ' + str(nums[len(nums) - 1])