n, m = map(int, input().split())

baskets = [x+1 for x in range(n)]

def flip(i,j):
    temp = baskets[i-1:j]
    temp.reverse()
    baskets[i-1:j] = temp

for _ in range(m):
    i, j = map(int,input().split())
    flip(i,j)

print(" ".join(list(map(str,baskets))))

# 1 2 3 4 5
# 2 1 3 4 5
# 2 1 4 3 5
# 3 4 1 2 5
# 3 4 1 2 5