N, M = map(int, input().split())

edges = []
for _ in range(M):
    x, y = map(int, input().split())
    edges.append((x, y))

visited = set()
count = 0


def dfs(root):
    global count

    visited.add(root)

    for edge in edges:
        if root in edge:
            opposite = edge[0] if root == edge[1] else edge[1]
            if opposite not in visited:
                count += 1
                dfs(opposite)


dfs(1)
print(count)
