nodes, colors = map(int, input().split())

# Create a matrix with all zeros
adjMatrix = [[0 for _ in range(nodes)] for _ in range(nodes)]
colMatrix = [-1 for _ in range(nodes)]

for i in range(nodes):
    row_values = list(map(int, input().split()))
    for j in range(nodes):
        adjMatrix[i][j] = row_values[j]
    
    
# Stack to store nodes for processing
stack = []
    
# Add the starting node to the stack
stack.append((0,0))
colMatrix[0]=0

traversed=1
solutions=0

def isPromising(k, color):
    l=0
    valid=True 
    while(l<k):
        if(colMatrix[l]==color and adjMatrix[k][l]==1):
            valid=False
        l+=1
    return valid    

def check_matrix(matrix, c):
    nums_in_matrix = set()
    for e in matrix:
        nums_in_matrix.add(e)
    
    required_nums = set(range(c))
    
    return required_nums.issubset(nums_in_matrix)

def DFS(cur_node):
    global traversed, solutions
    cur_node+=1
    if(cur_node>=nodes):       
        temp=stack.pop()
        if(check_matrix(colMatrix,colors)):
           solutions+=1       
        colMatrix[temp[0]]=-1
        return 0
    for i in range(colors):
        stack.append((cur_node,i))
        colMatrix[cur_node]=i
        traversed+=1
        if(isPromising(cur_node, i)):
          DFS(cur_node)
        else:
            temp=stack.pop()
            colMatrix[temp[0]]=-1
    temp=stack.pop()
    colMatrix[temp[0]]=-1
            
    return 0

DFS(0)

if(solutions==0):{
    print("no")
}
else:
    print(solutions*colors)
    print(traversed*colors)

    



   
        
