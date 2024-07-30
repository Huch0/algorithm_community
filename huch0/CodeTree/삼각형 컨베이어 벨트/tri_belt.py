n, t = map(int, input().split())
tri = []
tri.append(list(map(int, input().split())))
tri.append(list(map(int, input().split())))
tri.append(list(map(int, input().split())))


for _ in range(t):
    l = tri[-1][-1]
    for i in range(3):
        r = tri[i][-1]
        for j in range(n - 1, 0, -1):
            tri[i][j] = tri[i][j - 1]

        tri[i][0] = l
        l = r

for i in range(3):
    print(' '.join(map(str, tri[i])))
