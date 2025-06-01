import sys

input = sys.stdin.readline

A, B, D = map(int, input().split())

is_prime = [True] * (B+1)

is_prime[0] = is_prime[1] = False

for i in range(2, int(B ** 0.5) +1):
    if is_prime[i]:
        for j in range(i*i, B + 1, i):
            is_prime[j] = False
         
count = 0

for i in range(A, B+1):
    if is_prime[i]:
        if str(D) in str(i):
            count += 1
print(count)