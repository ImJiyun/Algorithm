import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dnas = [input().strip() for _ in range(N)]
result = ''
total_dist = 0

for i in range(M):
    counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for dna in dnas:
        counts[dna[i]] += 1
    
    max_count = max(counts.values())
    for char in 'ACGT':
        if counts[char] == max_count:
            result += char
            break
            
for dna in dnas:
    for i in range(M):
        if dna[i] != result[i]:
            total_dist += 1
            
print(result)
print(total_dist)