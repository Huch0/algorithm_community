import sys
n = int(sys.stdin.readline())
m = []
for i in range(n):
    m.append(list(map(int, sys.stdin.readline().split())))
m.sort(key=lambda x: (x[1], x[0]))
for i in m:
    print(i[0], i[1])