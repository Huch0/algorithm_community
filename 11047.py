N, K= map(int, input().split())

coins=[]
i=0
for _ in range(N):
    coin=int(input())
    coins.append(coin)
    if coin<=K:
        i=_

count=0
while K:
    K-=coins[i]
    count+=1
    while K<coins[i] and i>=0:
        i-=1
        
print(count)