import heapq
import sys

N, needed=map(int,sys.stdin.readline().split())

trees=[0]*N

trees = list(map(int, sys.stdin.readline().split()))

def cut(height):
    sum=0
    for t in trees:
        cut_len=t-height
        if cut_len>0:
            sum+=cut_len
    #print("Return for ", height," is ",sum)
    return sum

def binarySearch():
    end=max(trees)
    #print("end :", end)
    start=0
    #print("start :", start)
    mid=(end+start)//2
    #print("mid :", mid)
    while end-start >1:
        if needed<cut(mid):
            start=mid
        else:
             end=mid          
        mid=(end+start)//2
    mid+=1
    while 1:
        if cut(mid)<needed:
            mid-=1
        else:
            break
    print(mid)

binarySearch()