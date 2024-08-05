# 4 11
# 802
# 743
# 457
# 539

# parametric search

K, N = map(int, input().split())
Wires = []

for _ in range(K):
    Wires.append(int(input()))

def cal_num_of_wire(length):
    result = 0
    for w in Wires:
        result += w // length

    return result

st = 1
en = max(Wires) + 1

while st < en:
    mid = (st+en+1) // 2
    n_of_wire_by_mid = cal_num_of_wire(mid)
    if n_of_wire_by_mid < N:
        en = mid - 1
    else:
        st = mid

print(st)