# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2

# -> 5

# 5 2
# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 2 0 0 1 1
# 2 2 0 1 2

# -> 10

# 5 1
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0

# -> 11

# 5 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1

# -> 32

N, M = map(int, input().split())

p_house = []
p_chicken = []

for x in range(N):
    line = input().split()
    for y in range(N):
        if line[y] == "1":
            p_house.append((int(x), int(y)))
        elif line[y] == "2":
            p_chicken.append((int(x), int(y)))
            
d_house = []

def d(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

for p_h in p_house:
    distance = []
    for p_c in p_chicken:
        distance.append(d(p_h, p_c))
    d_house.append(distance)

C = len(p_chicken)
if C <= M:
    print(sum([min(d) for d in d_house]))
else:
    from itertools import combinations

    def mask(c, line):
        result = []
        for i in c:
            result.append(line[i])
        return result
    
    results = []
    for c in combinations(range(C), M):
        results.append(sum([min(mask(c, d)) for d in d_house]))

    print(min(results))