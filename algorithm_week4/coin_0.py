coin_type_num, money = map(int, input().split())
coin_type = []
coin_count = 0

for _ in range(coin_type_num):
    coin_type.append(int(input()))
    
coin_type.reverse()

for coin in coin_type:
    coin_count += money//coin
    money %= coin

print(coin_count)