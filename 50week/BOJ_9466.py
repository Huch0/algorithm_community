# 2
# 7
# 3 1 3 7 3 4 6
# 8
# 1 2 3 4 5 6 7 8
from collections import defaultdict, deque

class code_1:
    def __init__(self) -> None:
        pass
    def answer():
        T = int(input())
        answer = []
        for i in range(T):
            N = int(input())
            stud = list(map(int, input().split()))

            # 지칭하는 포인터 딕셔너리로 저장
            index = 1
            edges = defaultdict(int)
            for st in stud:
                edges[index] = st
                index += 1

            # 인접행렬처럼 생각해서 N번 지칭하는 방향대로 나아갈 것이다.
            for _ in range(N):
                for j in range(N):
                    stud[j] = edges[stud[j]]
            
            # 최종적으로 stud에 남아있는 서로 다른 원소의 개수를 세고 N에서 뺀다
            final_stud = set(stud)
            answer.append(N - len(final_stud))

        for a in answer:
            print(a)



# N
# 2 3 4 ... N 1

T = int(input())
answer = []
for _ in range(T):
    N = int(input())
    stud = list(map(int, input().split()))
    
    # Build the graph and calculate in-degrees
    edges = {}
    in_degree = [0] * (N + 1)
    for idx, st in enumerate(stud, 1):
        edges[idx] = st
        in_degree[st] += 1

    # Initialize the queue with nodes having in-degree 0
    queue = deque()
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)

    visited = [False] * (N + 1)
    while queue:
        u = queue.popleft()
        visited[u] = True
        v = edges[u]
        in_degree[v] -= 1
        if in_degree[v] == 0 and not visited[v]:
            queue.append(v)

    # Count the number of students not in any team (cycle)
    cnt = 0
    for i in range(1, N + 1):
        if not visited[i]:
            cnt += 1
    answer.append(N - cnt)

for a in answer:
    print(a)