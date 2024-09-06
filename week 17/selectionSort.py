import sys

# Set the recursion limit to 10000
sys.setrecursionlimit(10000)

def selectionSort(arr,n,k):
    sortedArr=[]
    for i in range(0, k):
        min=arr[0]
        index=0
        for j in range(0,n-i):
            if arr[j]<min:
                min=arr[j]
                index=j
        sortedArr.append(min)
        arr.insert(index,arr[0])
        arr.remove(min)
        arr.pop(0)     
    
    #print("sorted:")
    for e in sortedArr:
        print(e)
    #print("unsorted:")
    for e in arr:
        print(e)
    
sortType, k = map(int, input("input sort type(num) and kth:").split()) 
n=int(input("size of arrays:"))

arr=[]

for i in range(n):
    num=int(input("int for array:"))
    arr.append(num)
    selectionSort(arr,n,k)