# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
pay = int(input())
coins = [40, 20, 10, 5, 1]
min_coin = 0
for coin in coins:
	if pay < 0:
		break
	min_coin += pay // coin
	pay %= coin
	
print(min_coin)