import numpy as np
import sys
input = sys.stdin.readline

# Algorithm implementation
def floyd_warshall(G,nV):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(1,nV):
        for i in range(1,nV):
            for j in range(1,nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    return distance

N, c1, c2 = map(int, input().split())
vertex = np.full((N+1, N+1), 987654321)

for i in range(N-1):
    i, j, n= map(int, input().split())
    vertex[i][j]= n
    vertex[j][i]= n
    
distance=floyd_warshall(vertex,N+1)

row1=distance[c1]
row2=distance[c2]

spreadTime= np.full(N+1,9876543421)
for i in range(1,N+1):
    spreadTime[i]=min(row1[i],row2[i])

# Get the indices of the values in ascending order
sorted_indices = np.argsort(spreadTime)

for i in sorted_indices:
    if(i!=c1 and i!=c2 and i!=0):
        print(i)

 




