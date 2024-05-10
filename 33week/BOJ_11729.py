# N = 3

# 7
# 1 3
# 1 2
# 3 2
# 1 3
# 2 1
# 2 3
# 1 3

N = int(input())
def fun(n, start, end):
    if n == 1:
        print(str(start) + " " + str(end))
        return
    fun(n-1, start, 6 - start - end)
    fun(1, start, end)
    fun(n-1, 6 - start - end, end)

print(2**N - 1)
fun(N, 1, 3)