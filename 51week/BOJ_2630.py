# 8
# 1 1 0 0 0 0 1 1
# 1 1 0 0 0 0 1 1
# 0 0 0 0 1 1 0 0
# 0 0 0 0 1 1 0 0
# 1 0 0 0 1 1 1 1
# 0 1 0 0 1 1 1 1
# 0 0 1 1 1 1 1 1
# 0 0 1 1 1 1 1 1

# -> 9 / 7

N = int(input())
paper = []

for _ in range(N):
    line = list(map(int, input().split()))
    paper.append(line)

results = [0, 0]

def check_eq(x, y, n):
    first = paper[x][y]
    for i in range(n):
        for j in range(n):
            if paper[x+i][y+j] != first:
                return False
    return True

def func(x, y, n):
    if check_eq(x, y, n):
        results[paper[x][y]] += 1
    else:
        m = n // 2
        for i in range(2):
            for j in range(2):
                func(x + i*m, y + j*m, m)

func(0, 0, N)

for r in results:
    print(r)