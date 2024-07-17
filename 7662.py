t = int(input())

def insertionLocation(array, element):
    length=len(array)
    if length==0:
        return 0
    left=0
    right=length-1
    while(1):
        if array[left]>element:
            return left
        if array[right]<element:
            return right+1
        left+=1
        right-=1

for _ in range(t):
    n=int(input())
    PQueue=[]
    for i in range(n):
        command, priority = input().split()
        if(command=='I'):
            #PQueue.insert(insertionLocation(PQueue,int(priority)),int(priority))
            PQueue.append(int(priority))
        elif (command=='D'):
            if len(PQueue)==0:
                continue
            else:
                PQueue.sort()
                if priority=='1':
                    e=PQueue.pop()
                else:
                    e=PQueue.pop(0)
    if len(PQueue):
        print(PQueue[-1],' ', PQueue[0])
    else:
        print("EMPTY")