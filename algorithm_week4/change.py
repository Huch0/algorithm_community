coin_types = [500, 100, 50, 10, 5, 1]

price = int(input())
change = 1000 - price
num = 0

for coin in coin_types:
    num += change // coin
    change %= coin
    
print(num)