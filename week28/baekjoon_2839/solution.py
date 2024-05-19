N = int(input())
i = 0
j = 0

while(N % 5 != 0 and N > 0):
    i += 1
    N -= 3

if N % 5 == 0:
    j = N // 5
    print(i + j)
else:
    print(-1)