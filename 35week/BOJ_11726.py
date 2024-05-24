#첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

N = int(input())
D = [[0 for _ in range(N)] for _ in range(N+1)]

D[1][0] = 1

for i in range(2, N+1):
    D[i][0] = 1
    if i%2 == 0:
        D[i][i//2] = 1
    for j in range(1, N):
        if (i // 2) < j or D[i][j] > 0:
            break
        D[i][j] = D[i-2][j-1] + D[i-1][j]

sum = 0

for i in range(N):
    if D[N][i] == 0:
        break
    sum += (D[N][i] % 10007)

print(sum % 10007)