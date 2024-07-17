# 2
# 6
# 22

T = int(input())

quests = []

for _ in range(T):
    quests.append(int(input()))
m = max(quests)

if m != 0:
    D = [[0, 0] for _ in range(m+1)]

    D[0] = [1, 0]
    D[1] = [0, 1]

    for i in range(2, m+1):
        D[i][0] = D[i-1][0] + D[i-2][0]
        D[i][1] = D[i-1][1] + D[i-2][1]

    for q in quests:
        print(f"{D[q][0]} {D[q][1]}")

else: 
    for q in quests:
        print("1 0")
