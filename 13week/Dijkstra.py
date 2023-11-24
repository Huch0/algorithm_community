# Discription: Dijkstra Algorithm
# Date: 2023.11.24.

#setting
number_of_nodes = 6
INF = 999999999

graph = [
    [0, 2, 5, 1, INF, INF],
    [2, 0, 3, 2, INF, INF],
    [5, 3, 0, 3, 1, 5],
    [1, 2, 3, 0, 1, INF],
    [INF, INF, 1, 1, 0, 2],
    [INF, INF, 5, INF, 2, 0]
]

visited = [False, False, False, False, False, False]
distance = []

def get_small_index():
    min = INF
    index = 0
    for i in range(len(distance)):
        if distance[i] < min and visited[i] == False:
            min = distance[i]
            index = i
    return index

def dijkstra(start):
    global distance
    global visited
    distance = graph[start]
    visited[start] = True

    for i in range(number_of_nodes - 2):
        current = get_small_index()
        visited[current] = True
        for j in range(number_of_nodes):
            if visited[j] == False:
                if distance[current] + graph[current][j] < distance[j]:
                    distance[j] = distance[current] + graph[current][j]

    visited = [False, False, False, False, False, False]

dijkstra(0)
print(distance)