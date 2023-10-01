graph = [
    [], # 인덱스와 노드 번호를 일치시키기 위해 편의상 첫 원소는 비움.
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

# 그래프와 방문 여부 리스트가 필요함.
# dfs, bfs의 핵심은 재귀함수. 재귀함수의 내용도 별 거 없음. 그냥 방문하고 재귀함수를 호출하면 됨.

def dfs(graph, v, visited): # 그래프, 노드, 방문여부를 파라미터로 받는다
    visited[v] = True # 가장 먼저 해당 노드 방문 처리를 해야함.
    print(v, end = ' ') # 탐색 순서 출력
    
    for i in graph[v]:
        if not visited[i]: # base condition. 이 표현 자주 쓰인다. boolean list visited의 특정 원소가 False라면!!
            dfs(graph, i, visited) # dfs의 핵심. 재귀함수를 호출.
            
dfs(graph, 1, visited)