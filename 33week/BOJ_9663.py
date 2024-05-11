N = int(input())

# back tracking

col_used = [False] * N
dia_used1 = [False] * (2*N - 1)
dia_used2 = [False] * (2*N - 1)

count = 0

def fun(row):
    global count
    if row == N:
        count += 1
        return
    
    for i in range(N):
        if not (col_used[i] or dia_used1[row+i] or dia_used2[N-1+row-i]):
            col_used[i] = True
            dia_used1[row+i] = True
            dia_used2[N-1+row-i] = True
            fun(row+1)
            col_used[i] = False
            dia_used1[row+i] = False
            dia_used2[N-1+row-i] = False

fun(0)
print(count)