# 10
# 1 100 2 50 60 3 5 6 7 8

# -> 113

N = int(input())
numbers = list(map(int, input().split()))

plus_numbers = [0 for _ in range(N)]
cp_numbers = numbers[::]

D = [0 for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):        
        if numbers[j] > numbers[i] and plus_numbers[j] < numbers[i] + plus_numbers[i]:
            plus_numbers[j] =  numbers[i] + plus_numbers[i]
            cp_numbers[j] = numbers[j] + plus_numbers[j]
    D[i] = max(cp_numbers)

print(D[N-1])