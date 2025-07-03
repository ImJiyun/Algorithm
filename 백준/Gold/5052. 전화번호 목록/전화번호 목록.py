import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    phone_numbers = [input().strip() for _ in range(n)]
    phone_numbers.sort()
    
    found = False
    for i in range(len(phone_numbers)-1):
        if phone_numbers[i+1].startswith(phone_numbers[i]):
            found = True
            break
    if found:
        print('NO')
    else:
        print('YES')