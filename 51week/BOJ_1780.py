# 9
# 0 0 0 1 1 1 -1 -1 -1
# 0 0 0 1 1 1 -1 -1 -1
# 0 0 0 1 1 1 -1 -1 -1
# 1 1 1 0 0 0 0 0 0
# 1 1 1 0 0 0 0 0 0
# 1 1 1 0 0 0 0 0 0
# 0 1 -1 0 1 -1 0 1 -1
# 0 -1 1 0 1 -1 0 1 -1
# 0 1 -1 1 0 -1 0 1 -1
import math

N = int(input())
paper = []

for _ in range(N):
    line = list(map(int, input().split()))
    paper.append(line)

results = [0, 0, 0]

def check_same(x, y, n):
    first = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != first:
                return False
    return True

def func(x, y, n):
    # 아...
    # 이거 Base condition을 주변 종이가 다 같을 때까지로 잡아야함. 
    # 그러면 편해...

    if check_same(x, y, n):
        results[paper[x][y] + 1] += 1
    else:
        m = n // 3
        for i in range(3):
            for j in range(3):
                func(x + i * m, y + j * m, m)

func(0, 0, N)

for r in results:
    print(r)