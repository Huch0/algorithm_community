import collections

m = int(input())
n = int(input())

bridge = collections.defaultdict(list)

for _ in range(n): 
    a, b = list(map(int,input().split()))
    bridge[a].append(b)
    bridge[b].append(a)
    
traced = set()
visited = set()

def dfs(start) :
    if start in traced : return
    if start in visited : return
    
    traced.add(start)
    visited.add(start)
    
    for i in bridge[start] :
        dfs(i)
    traced.remove(start)

    return  

dfs(1)


print(len(visited)-1)