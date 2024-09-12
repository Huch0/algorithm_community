sum = 0 # set sum zero
for i in range(1, 1000001, 2): # for loop -> odd이기 때문에 interval is 2
    for j in str(i): # for loop : string으로 변환
        sum += int(j) # sum of the digits : 숫자를 더해야하기떄문에 int로 변환
print("The sum of the digits of odd numbers")
print(f"From 1 to one million is {sum:,}.")