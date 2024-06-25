# test code
# undirected graph
graph = [ [],
         [[1, 1, 2], [3, 1, 1]],
         [[3, 2, 3], [6, 2, 4]],
         [[4, 3, 4], [2, 3, 5]],
         [[5, 4, 5]]]

#Prim's Algorithm
import heapq

def prim(graph, start):
    mst = []
    visited = [False] * (len(graph)+1)
    heap = []
    visited[start] = True
    for i in graph[start]:
        heapq.heappush(heap, i)
    while heap:
        w, n1, n2 = heapq.heappop(heap)
        if visited[n2] == False:
            visited[n2] = True
            mst.append((n1, n2, w))
            for i in graph[n2]:
                heapq.heappush(heap, i)
    return mst

print()
print()
print("Prim's Algorithm")
print("---------------------------------------------------------")
print(prim(graph, 1))
# drawing spanning Tree and original graph code using networkx

import networkx as nx

G = nx.Graph()
for i in range(1, len(graph)):
    for j in graph[i]:
        G.add_edge(j[0], j[1], weight=j[2])

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edge_labels(G, pos)
nx.draw(G, pos, with_labels=True)

print("---------------------------------------------------------")

