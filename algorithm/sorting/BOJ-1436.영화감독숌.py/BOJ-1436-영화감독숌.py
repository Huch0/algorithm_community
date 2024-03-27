import sys

def Range(end) :
    List = []
    if end == 10 :
        for i in range(10) : List.append(i)
    
    elif end == 100 :
        for i in range(100) : List.append(i)
        for i in range(10) :
            List.append("0"+str(i))
    
    elif end == 1000 :
        for i in range(1000) : List.append(i)
        for i in range(10) :
            List.append("00"+str(i))
        for i in range(100) :
            List.append("0"+str(i))
    
    elif end == 10000 :
        for i in range(1000) : List.append(i)
        for i in range(10) :
            List.append("00"+str(i))
        for i in range(100) :
            List.append("00"+str(i))
        for i in range(1000) :
            List.append("0"+str(i))
    
    return List
        
    

n = int(sys.stdin.readline())
List = set()
List.add(666)

for i in range(1,10000) :
    List.add(int(str(i)+"666"))
    
for i in range(1,10) :
    for j in Range(1000) :
        List.add(int(str(i)+"666"+str(j)))

for i in range(1,100) :
    for j in Range(100) :
        List.add(int(str(i)+"666"+str(j)))

for i in range(1,1000) :
    for j in Range(10) :
        List.add(int(str(i)+"666"+str(j)))
        
for j in Range(10000) :
    List.add(int("666"+str(j)))

Sorted_List = list(List)
Sorted_List.sort()

print(Sorted_List[n-1])
            