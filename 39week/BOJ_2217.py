# 2
# 10
# 15

N = int(input())

ropes = []
for _ in range(N):
    ropes.append(int(input()))

ropes.sort()

state = ropes[-1]
for i in range(N-2, -1, -1):
    new_state = ropes[i] * (N-i)
    state = max(new_state, state)

print(state)