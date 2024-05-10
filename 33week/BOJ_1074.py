# 2 3 1 -> 14

# 1 ≤ N ≤ 15
# 0 ≤ r, c < 2**N

N, r, c = map(int, input().split())

def fun(x, y, n):
    if n == 1:
        return 2*x + y

    return 4**(n-1) * (2*(x // 2**(n-1)) + y // 2**(n-1)) + fun(x % 2**(n-1), y % 2**(n-1), n-1)

print(fun(r, c, N))