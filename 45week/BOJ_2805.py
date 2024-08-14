# 4 7
# 20 15 10 17
# -> 15

# 5 20
# 4 42 40 26 46
# -> 36

N, M = map(int, input().split())

trees = list(map(int, input().split()))

def cal_max_trees_by_H(h):
    return sum([max(0, tree - h) for tree in trees])

st = 0
en = max(trees)

while st < en:
    mid = (st + en + 1) // 2
    if cal_max_trees_by_H(mid) >= M:
        st = mid
    else:
        en = mid - 1
    
print(st)
    
