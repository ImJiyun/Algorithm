from collections import defaultdict

def solution(nums):
    goal = len(nums) // 2          
    kinds = len(set(nums))         
    return min(goal, kinds)