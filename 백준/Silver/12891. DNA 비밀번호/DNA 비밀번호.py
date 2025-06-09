import sys
from collections import defaultdict 
input = sys.stdin.readline

S, P = map(int, input().split())

line = input().strip()

A, C, G, T = map(int, input().split())

d = defaultdict(int)
alphabets = {'A': A, 'C': C, 'G': G, 'T': T}

count = 0

left, right = 0, P - 1
for i in range(left, right + 1):
    d[line[i]] += 1

def is_valid():
    for char in 'ACGT':
        if d[char] < alphabets[char]:
            return False
    return True
        
if is_valid():
    count += 1
    
while right < S-1:
    d[line[left]] -= 1
    left += 1
    right += 1
    d[line[right]] += 1
    
    if is_valid():
        count += 1

print(count)