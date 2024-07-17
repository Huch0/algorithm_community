# 12 -> 2731

N = int(input())
if N == 1:
    print(1)

else:
    D = [0 for _ in range(N+1)]

    D[1] = 1
    D[2] = 3

    for i in range(3, N+1):
        D[i] = (2*D[i-2] + D[i-1]) % 10007
    
    print(D[N])
