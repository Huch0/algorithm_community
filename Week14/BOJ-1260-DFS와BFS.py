import collections

n, edge, start = list(map(int,input().split()))

bridge = collections.defaultdict(list)

for _ in range(edge) :
    a,b = list(map(int,input().split()))
    bridge[a].append(b)
    bridge[b].append(a)

dfs_bridge = bridge.copy()
bfs_bridge = bridge.copy()

#dfs
dfs_result = []
dfs_discoverd = set()

def dfs(node) :
    if len(dfs_result) == n : return 
    
    if node in dfs_discoverd : return
    
    dfs_result.append(node)
    dfs_discoverd.add(node)
    
    dfs_bridge[node].sort()
    
    for i in dfs_bridge[node] :
        dfs(i)
    
    return

dfs(start)

#bfs
bfs_result = []
queue = collections.deque()
bfs_discoverd = set()

queue.append(start)

while queue :
    pop = queue.popleft()
    if pop in bfs_discoverd : continue
    
    bfs_result.append(pop)
    bfs_discoverd.add(pop)
    
    for i in bfs_bridge[pop] :
        if i not in bfs_discoverd : queue.append(i)

for i in dfs_result :
    print(i,end = " ")
    
print()

for i in bfs_result :
    print(i,end = " ")



        
        
