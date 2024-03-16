import sys

def check(previous, n) :
    for i in range(previous-1, n, -1) :
        if i not in discovered : return False    
    return True

n = int(sys.stdin.readline())

stack = 0
result = []
discovered = set()

previous = 0
flag = 0

for i in range(n):
    n = int(sys.stdin.readline())
    
    if i == 0 : 
        for j in range(n) :
            result.append("+")
        result.append("-")
        
        stack=n
        
    else : 
        if previous < n :
            for j in range(n-stack) :
                result.append("+")
            result.append("-")
            stack = n
        
        else : 

            if check(previous,n) : 
                result.append("-")
            else : 
                flag = 1
                break
    
    discovered.add(n)
    previous = n
    
if flag : print("NO")
else : 
    for i in result :
        print(i)
    
    
