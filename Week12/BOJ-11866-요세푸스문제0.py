def dfs(input_list, k):
    stack = []
    index = -1

    while len(input_list) > 0:
        index = (index + k) % len(input_list)
        stack.append(input_list.pop(index))
        index -= 1

    return stack

n, k = list(map(int, input().split()))
result_stack = dfs(list(range(1, n + 1)), k)
print("<", end = "")
for i in range(n-1) :
    print(result_stack[i], end = ", ")
print(result_stack[n-1], end=">")

"""
using recursion

def dfs(input_list, index) : 
    if len(input_list) == 1 : 
        stack.append(input_list.pop())
        return
    
    index = (index + k) % len(input_list)

    #while index > len(input_list) - 1 :
        #index = index - len(input_list) 
    stack.append(input_list.pop(index))
    index -= 1
    dfs(input_list,index)
    
n, k = list(map(int,input().split()))
stack = []
dfs([i for i in range(1,n+1)],-1)

print("<", end = "")
for i in range(n-1) :
    print(result_stack[i], end = ", ")
print(result_stack[n-1], end=">")

"""