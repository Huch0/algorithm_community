# 6
# 10 20 10 30 20 50
# -> 4

N = int(input())
line = list(map(int, input().split()))

D = [0 for _ in range(N)]

D[0] = 1

for i in range(1, N):
    for j in range(i):
        if line[i] > line[j]:
            D[i] = max(D[j], D[i])    
    D[i] += 1
    
print(max(D))