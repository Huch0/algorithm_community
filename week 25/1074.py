N, r, c=map(int, input().split())

count=0

while(N>0):
    thresh=2**(N-1)-1
    if r>thresh:
        if c>thresh:
            #quadrant=4
            count+=(thresh+1)*(thresh+1)*3
            r-=thresh+1
            c-=thresh+1
        else:
            #quadrant=3
            count+=(thresh+1)*(thresh+1)*2
            r-=thresh+1
    else:
        if c>thresh:
            #quadrant=1
            count+=(thresh+1)*(thresh+1)
            c-=thresh+1
        else:
            #quadrant=2   
    N-=1

print(count)
