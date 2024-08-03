n = int(input())
jenga = []
for _ in range(n):
    jenga.append(int(input()))

removes = []
for _ in range(2):
    removes.append(list(map(int, input().split())))


n_blocks = n
for s, e in removes:
    jenga[s-1:e] = [0] * (e - s + 1)
    n_blocks -= e - s + 1
    jenga = [block for block in jenga if block > 0]


print(n_blocks)
for block in jenga:
    print(block)
