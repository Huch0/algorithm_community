computer_n = int(input())
edges_n = int(input())

graph = [[] for _ in range(computer_n+1)]

for i in range(edges_n):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

visited = [-1] * (computer_n+1)
stack = [1]
count = -1
    
while stack:
    node = stack.pop()
    if visited[node] != 1:
        visited[node] = 1
        count += 1
        for next_node in graph[node]:
            stack.append(next_node)
            
print(count)
    
