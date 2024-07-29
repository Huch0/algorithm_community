n, t = map(int, input().split())
belt = []
belt.append(list(map(int, input().split())))
belt.append(list(map(int, input().split())))


for i in range(t):
    tmp = belt[1][- 1]
    # Push second line to right
    for i in range(n - 2, -1, -1):
        belt[1][i + 1] = belt[1][i]

    belt[1][0] = belt[0][-1]
    # Push first line to right
    for i in range(n - 2, -1, -1):
        belt[0][i + 1] = belt[0][i]

    belt[0][0] = tmp

for line in belt:
    print(' '.join(map(str, line)))
