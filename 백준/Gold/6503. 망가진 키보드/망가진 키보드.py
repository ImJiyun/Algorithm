import sys
from collections import defaultdict
input = sys.stdin.readline

while True:
    m = int(input())
    if m == 0:
        break
    chars = list(input().rstrip())
    cnts = defaultdict(int)
    left, right, n, max_length = 0, 0, len(chars), 0
    while right < n:
        cnts[chars[right]] += 1
        while len(cnts) > m:
            cnts[chars[left]] -= 1 
            if cnts[chars[left]] == 0:
                del cnts[chars[left]]
            left += 1
        max_length = max(max_length, right-left+1)
        right += 1
    print(max_length)    