import sys

def empty(List):
    if(len(List) == 0) : return 1
    else : return 0

n = int(sys.stdin.readline())
List = [] # create a list to use as a stack

for i in range(n) :
    Input = list(sys.stdin.readline().split())
    
    if (len(Input) == 2) : 
        List.append(int(Input[1]))
        
    else :
        if (Input[0] == "pop") :
            if(empty(List)) : print(-1)
            else : print(List.pop())
        
        elif (Input[0] == "size") :
            print(len(List))
        
        elif (Input[0] == "empty") :
            print(empty(List))
        
        elif(Input[0] == "top"):
            if(empty(List)) : print(-1)
            else : print(List[-1])