import sys
input = sys.stdin.readline

M, N = map(int, input().strip().split(" "))

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(M, N+1):
    if isPrime(i):
        print(i)