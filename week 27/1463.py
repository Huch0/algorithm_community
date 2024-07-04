import sys
input = sys.stdin.readline

i = int(input().rstrip())

A = [987654321] * 1000001
A[1]=0

j=2
while(j!=i+1):
    if j%3==0:
        temp=min(A[int(j/3)]+1,A[j-1]+1)
    else:
        temp=A[j-1]+1
    if j%2==0:
        A[j]=min(temp,A[int(j/2)]+1)
    else:
        A[j]=temp
    j+=1

for a in range(1,i+1):
    print(a,"=",A[a])
#print(A[i])
