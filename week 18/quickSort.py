import heapq
import sys

# Set the recursion limit to 10000
sys.setrecursionlimit(10000)

def partition(low, high):
    global arr
    left = low
    right = high
    pivot = arr[low]

    while left <= right:
        while left <= high and arr[left] <= pivot:
            left += 1
        while right > low and arr[right] > pivot:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]
    return right


# Declare global variables here
found = False
pivot_count = 0

def quickSort(low, high):
    global pivot_count, k, found, arr  # Assuming these are global variables
    if low >= high:
        return
    pivot = partition(low, high)
    pivot_count += 1

    if pivot_count == k:
        found = True
        for val in arr:
            print(val)
    quickSort(low, pivot - 1)
    quickSort(pivot + 1, high)  
    

sortType, k = map(int, input("input sort type(num) and kth:").split()) 
n=int(input("size of arrays:"))

arr=[]

for i in range(n):
    num=int(input("int for array:"))
    arr.append(num)
    selectionSort(arr,n,k)