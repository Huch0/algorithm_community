# ***
# * *
# ***

N = int(input())

stars = [[0 for _ in range(N)] for _ in range(N)]

def func(x, y, n):
    if n == 3:
        for i in range(3):
            for j in range(3):
                if i!=1 or j!=1:
                    stars[x + i][y + j] = 1
    else:
        m = n//3
        for i in range(3):
            for j in range(3):
                if i!=1 or j!=1:
                    func(x + m*i, y + m*j, m)

func(0, 0, N)

for star in stars:
    for s in star:
        if s == 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()