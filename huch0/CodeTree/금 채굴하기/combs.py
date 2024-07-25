from itertools import combinations_with_replacement

n, m = map(int, input().split())
mat = []

for _ in range(n):
    mat.append(list(map(int, input().split())))

# Make masks
combs = list(combinations_with_replacement(range(-n, n + 1), 2))
masks = [[] for _ in range(n + 1)]
for c in combs:
    i = sum(map(abs, c)) # Manhattan distance
    if i <= n:
        masks[i].append(c)
        if c[0] != c[1]: # if x == y, no need to append reversed one
            masks[i].append(tuple(reversed(c)))

max_coin = 0
for i in range(n):
    for j in range(n):
        coins = 0
        for K in range(n + 1):
            profit = -(K * K + (K + 1) * (K + 1))
            for dx, dy in masks[K]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < n:
                    coins += mat[nx][ny]
            profit += m * coins
            if profit >= 0:
                max_coin = max(max_coin, coins)

print(max_coin)
