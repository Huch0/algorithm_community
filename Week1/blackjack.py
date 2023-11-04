n, blackjack = list(map(int,input().split()))
num_list = list(map(int,input().split()))
max = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if num_list[i]+ num_list[j] + num_list[k] <= blackjack and num_list[i]+ num_list[j] + num_list[k] > max :
                max = num_list[i]+ num_list[j] + num_list[k]

print(max)