def coin_exchange(coins, amount):
    # Descending order
    coins.sort(reverse=True)
    n_coins = 0
    for coin in coins:
        n_coins += amount // coin
        amount %= coin
    return n_coins


if __name__ == "__main__":
    coins = [1, 5, 10, 50, 100, 500]
    amount = 620
    print("# of coins :", coin_exchange(coins, amount))
