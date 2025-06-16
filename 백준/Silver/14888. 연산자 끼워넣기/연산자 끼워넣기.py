import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
ops = list(map(int, input().split()))
operators = []

for i, count in enumerate(ops):
    if i == 0:
        operators.extend(['+'] * count)
    elif i == 1:
        operators.extend(['-'] * count)
    elif i == 2:
        operators.extend(['*'] * count)
    else:
        operators.extend(['/'] * count)

arr = []
visited = [False] * (N-1)

max_value, min_value = float('-inf'), float('inf')

def permute():
    global max_value, min_value
    if len(arr) == N-1:
        total = A[0]
        for i in range(N-1):
            op = arr[i]
            if op == '+':
                total += A[i+1]
            elif op == '-':
                total -= A[i+1]
            elif op == '*':
                total *= A[i+1]
            else:
                if total < 0:
                    total = -(-total // A[i + 1])
                else:
                    total = total // A[i + 1]

        max_value = max(max_value, total)
        min_value = min(min_value, total)
        return
    for i in range(len(operators)):
        if visited[i]:
            continue
        visited[i] = True
        arr.append(operators[i])
        permute()
        arr.pop()
        visited[i] = False
        
permute()      
print(max_value)
print(min_value)