import collections

N = int(input())
num_list = collections.Counter(map(int,input().split()))

M = int(input())
find = list(map(int,input().split()))

for num in find :
    print(num_list[num], end=" ")
    
