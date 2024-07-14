n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

ans = []
for i in range(n):
    for j in range(n):
        start = [i, j]
        stack = [start]
        cnt = 0
        while stack:
            node = stack.pop()
        
            if 0 < node[0] - 1 < n and 0 < node[1] < n and graph[node[0] - 1][node[1]] == 1:
                stack.append([node[0] - 1, node[1]])
                graph[node[0] - 1][node[1]] = 0
                done = False
                cnt += 1
            if 0 < node[0] + 1 < n and 0 < node[1] < n and graph[node[0]+ 1][node[1]] == 1:
                stack.append([node[0] + 1, node[1]])
                graph[node[0] + 1][node[1]] = 0
                done = False
                cnt += 1
            if 0 < node[0] < n and 0 < node[1] - 1 < n and graph[node[0]][node[1] - 1] == 1:
                stack.append([node[0],node[1] - 1])
                graph[node[0]][node[1] - 1] = 0
                done = False
                cnt += 1
            if 0 < node[0] < n and 0 < node[1] + 1 < n and graph[node[0]][node[1] + 1] == 1:
                stack.append([node[0], node[1] + 1])
                graph[node[0]][node[1] + 1] = 0
                done = False
                cnt += 1
        if len(stack) > 0:
            ans.append(len(stack))
            
print(len(ans))
for node in ans:
    print(len(node))
