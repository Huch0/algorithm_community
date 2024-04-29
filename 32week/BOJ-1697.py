# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 
# 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 
# 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

# 5 17 -> 4
from collections import deque

N, K = map(int, input().split())

queue = deque()
distance = [-1] *100001

queue.append(N)
distance[N] = 0

same_flag = (N==K)

if same_flag:
    print(0)
else:
    while queue:
        cur_x = queue.popleft()

        for i in range(3):
            nx = 0
            if i == 0:
                nx = cur_x + 1
            elif i == 1:
                nx = cur_x - 1
            else:
                nx = cur_x * 2
            if nx < 0 or nx > 100000:
                continue
            if distance[nx] >= 0:
                continue
            if nx == K:
                print(distance[cur_x] + 1)
                queue.clear()
                break
            distance[nx] = distance[cur_x] + 1
            queue.append(nx)    