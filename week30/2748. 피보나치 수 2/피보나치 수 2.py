from collections import deque

N = int(input())

fib = deque()
fib.append(0)
fib.append(1)

for _ in range(2, N+1):
    fib.append(sum(fib))
    fib.popleft()
    
    
print(fib.pop())
