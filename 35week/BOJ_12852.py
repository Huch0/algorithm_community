# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

# 2
# -> 1 / 2 1

# 10
# -> 3 / 10 9 3 1

N = int(input())

# BFS
D = [0 for _ in range(N+1)]

from collections import deque
from copy import deepcopy

queue = deque()
queue.append([N])

result = []
while queue:
    path = queue.popleft()
    cur_x = path[-1]

    path3 = deepcopy(path)
    path2 = deepcopy(path)
    path1 = deepcopy(path)
    
    if cur_x % 3 == 0:
        if D[cur_x // 3] == 0:
            D[cur_x // 3] = D[cur_x] + 1
            path3.append(cur_x // 3)
            queue.append(path3)
    
    if cur_x % 2 == 0:
        if D[cur_x // 2] == 0:
            D[cur_x // 2] = D[cur_x] + 1
            path2.append(cur_x // 2)
            queue.append(path2)
    
    if D[cur_x-1] == 0:
        D[cur_x-1] = D[cur_x] + 1
        path1.append(cur_x-1)
        queue.append(path1)

    if D[1] > 0:
        dq_list = list(queue)
        len_dq = len(dq_list)
        for q in dq_list:
            if q[-1] == 1:
                result = q
        break

if N != 1:
    print(D[1])
    for r in result:
        print(r, end = " ")
    print()
else:
    print(0)
    print(1)