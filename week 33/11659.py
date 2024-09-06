N, M =map(int, input().split())

numbers = list(map(int, input().split()))

dp_sum=[numbers[0]]*N

for i in range(1,N):
    dp_sum[i]=dp_sum[i-1]+numbers[i]
    
for _ in range(M):
    left, right = map(int, input().split())
    print(dp_sum[right-1]-dp_sum[left-1]+numbers[left-1])