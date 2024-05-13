from itertools import combinations

# 7 1 2 3 4 5 6 7
# 8 1 2 3 5 8 13 21 34
# 0

lottos = []

line = input()
while line != "0":
    lottos.append(line.split()[1:])
    line = input()
    
for lotto in lottos:
    perm = list(combinations(lotto, 6))
    for p in perm:
        #print(p)
        for n in p:
            print(n, end = " ")
        print()
    print()