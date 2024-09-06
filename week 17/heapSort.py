import heapq

def heapSort(arr,n,k):
    # Convert the input list into a heap
    heapq.heapify(arr)
    
    # Create an empty list to store the sorted elements
    sorted_arr = []
    #print(arr)
    # Repeatedly pop elements from the heap and append them to the sorted list
    count=0
    
    while arr:
        sorted_arr.append(heapq.heappop(arr))
        count+=1
        if(count==k):
            break
    for e in arr:
        print(e)
        
sortType, k = map(int, input("input sort type(num) and kth:").split()) 
n=int(input("size of arrays:"))

arr=[]

for i in range(n):
    num=int(input("int for array:"))
    arr.append(num)


heapSort(arr,n,k)