import sys

input = sys.stdin.readline

MAX = 10000
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX ** 0.5) + 1):
    if is_prime[i]: # i가 소수면
        # i의 배수는 소수가 아님
        for j in range(i * i, MAX + 1, i):
            is_prime[j] = False

T = int(input())

for _ in range(T):
    n = int(input())
    for i in range(n // 2, 1, -1):
        if is_prime[i] and is_prime[n - i]:
            print(i, n - i)
            break