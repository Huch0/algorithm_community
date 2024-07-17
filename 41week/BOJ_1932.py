# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5

D = []

N = int(input())

for i in range(N):
    line = input().split()
    line = [int(l) for l in line]
    if i == 0:
        D.append(line)
    else:
        line[0] += D[-1][0]
        line[i] += D[-1][i-1]
        for j in range(1, i):
            line[j] += max(D[-1][j], D[-1][j-1])
        D.append(line)

print(max(D[-1]))
# if N == 1:
#     print(D[0])

# else:
#     for i in range(1, N):
#         for j in range(0, i+1):
#             D[i][j] = D[]
