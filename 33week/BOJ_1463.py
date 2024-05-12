# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

# BFS

# from collections import deque

# N = int(input())

# queue = deque()
# distance = [-1] * (N+1)
# queue.append(N)
# distance[N] = 0

# while queue:
#     cur_x = queue.popleft()
#     if distance[1] > 0:
#         break
#     if distance[cur_x//3] < 0 and cur_x % 3 == 0:
#         distance[cur_x//3] = distance[cur_x] + 1
#         queue.append(cur_x//3)
#     if distance[cur_x//2] < 0 and cur_x % 2 == 0:
#         distance[cur_x//2] = distance[cur_x] + 1
#         queue.append(cur_x//2)
#     if distance[cur_x - 1] < 0 and cur_x - 1 > 0:
#         distance[cur_x - 1] = distance[cur_x] + 1
#         queue.append(cur_x - 1)

# print(distance[1])

# DP

N = int(input())
dist = [-1] * (N+1)

dist[1] = 0
for i in range(2, N+1):
    dist[i] = dist[i-1] + 1
    if i % 2 == 0:
        dist[i] = min(dist[i], dist[i//2] + 1)
    if i % 3 == 0:
        dist[i] = min(dist[i], dist[i//3] + 1)

print(dist[N])