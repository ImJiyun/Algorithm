import sys
input = sys.stdin.readline

def combine(idx, nums, arr):
    if len(arr) == 6:
        print(' '.join(map(str, arr)))
        return
    for i in range(idx, len(nums)):
        combine(i+1, nums, arr + [nums[i]])

firstLine = True
while True:
    nums = list(map(int, input().split()))
    N = nums[0]
    if N == 0:
        break
    if not firstLine:
        print()
    firstLine = False
    combine(0, nums[1:], [])