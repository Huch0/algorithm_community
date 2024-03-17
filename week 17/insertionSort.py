import sys

# Set the recursion limit to 10000
sys.setrecursionlimit(10000)

def insertionSort(arr,k):
    count=0
    for i in range(1, len(arr)):
        key = arr[i]
        j = 0
        # Move elements of arr[0..i-1] that are less than key
        # one position to the right to make space for key
        count+=1
        while j < i and arr[j] < key:
            count+=1
            j += 1
        # Insert key at the correct position
        arr[j+1:i+1] = arr[j:i]
        arr[j] = key
    print(arr)
    
sortType, k = map(int, input("input sort type(num) and kth:").split()) 
n=int(input("size of arrays:"))

arr=[]

for i in range(n):
    num=int(input("int for array:"))
    arr.append(num)
    insertionSort(arr,k)
    
