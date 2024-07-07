N, M = map(int, input().split())

neverHeard=[]
neverSeenorHeard=[]

for i in range(N):
    temp=input()
    neverHeard.append(temp)

neverHeard.sort()

def binSearch(string):
    l=0
    r=len(neverHeard)-1
    while(l+1<r):
        mid=int((l+r)/2)
        if neverHeard[mid]==string:
            return True
        if neverHeard[mid]<string:
            l=mid
        else:
            r=mid
    if (neverHeard[l]==string) or (neverHeard[r]==string):
        return True
    return False

for j in range(M):
    temp=input()
    if(binSearch(temp)):
        neverSeenorHeard.append(temp)
 
neverSeenorHeard.sort()
        
print(len(neverSeenorHeard))
for e in neverSeenorHeard:
    print(e)
