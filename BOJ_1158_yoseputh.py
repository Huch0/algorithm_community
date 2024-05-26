N, K = map(int,input().split())

numlist = [str(x+1) for x in range(N)]
permutation = []
i = 0 

for _ in range(N):
    i = (i + K - 1) % len(numlist)
    permutation.append(numlist.pop(i))

print("<"+", ".join(permutation)+">")
