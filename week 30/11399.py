N=int(input())

line=list(map(int,input().split()))
line.sort()

waitingTime=0
for e in line:
    waitingTime+=e*N
    N-=1
print(waitingTime)