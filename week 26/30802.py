N=int(input())
shirts = [int(x) for x in input().split()]
T, P= map(int,input().split())

sum=0
for e in shirts:
    sum+=(e+T-1)//T
print(sum)

print(N//P,N%P)