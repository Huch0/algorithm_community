def plusArr(arr):
    returnArr=arr.copy()
    for i in range(len(returnArr)):
        if returnArr[i]<0:
            returnArr[i]=-returnArr[i]
    return returnArr
            
def isCons(arr):
    a=1
    for e in arr:
        if a==e:
            a+=1
            continue
        else:
            return False
    return True

def swap(arr, i, j):
    returnArr=arr.copy()
    if (i==-1) and (j==-1):
        return returnArr
    while(i<=j):
        returnArr[i],returnArr[j]=-returnArr[j],-returnArr[i]
        i+=1
        j-=1
    return returnArr

def begin_End(arr):
    b=-1
    e=-1
    plus=plusArr(arr)
    
    for i in range(len(arr)):
        if plus[i] != i+1: #checks if it is not in order, index+1=value
            b=i
            for j in range(i+1, len(arr)):
                if plus[j]==b+1:
                    e=j
                    break
            break
        
    if b==-1:
        for i in range(len(arr)):
            if arr[i]<0:
                return i,i
    
    return b,e

def begin_End2(arr):
    b=-1
    e=-1
    plus2=plusArr(arr)
    for i in range(len(plus2) - 1, -1, -1):
        if plus2[i] != i+1:
            e=i
            for j in range(i, -1, -1):
                if plus2[j] == e+1:
                    b=j
                    break
            break
        
    return b,e

def result(arr):
    t1=swap(arr, begin_End(arr)[0], begin_End(arr)[1])   
    t2=swap(arr, begin_End2(arr)[0], begin_End2(arr)[1])
    
    if(isCons(t1)):
        print("one")
    elif isCons(swap(t1, begin_End(t1)[0], begin_End(t1)[1])):
        print("two")
    elif isCons(swap(t2, begin_End(t2)[0], begin_End(t2)[1])): 
        print("two")
    else:
        print("over")
        

k = int(input())

Fish = []

for i in range(5):
    numbers = list(map(int, input().split()))
    Fish.append(numbers)
    result(numbers)



#i=1
#for arr in Fish:
#    print("arr",i)
#    for e in arr:
#        print(e," ")
#    i+=1
    