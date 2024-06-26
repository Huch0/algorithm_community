# 5 4 4
# 3 3
# 1 0 1
# 1 1 1
# 1 0 1
# 2 5
# 1 1 1 1 1
# 0 0 0 1 0
# 2 3
# 1 1 1
# 1 0 1
# 3 3
# 1 0 0
# 1 1 1
# 1 0 0

N, M, K = map(int, input().split())

notebook = [[0 for _ in range(M)] for _ in range(N)]
stickers = []

for i in range(K):
    n, m = map(int, input().split())
    sticker = []
    for _ in range(n):
        line = input().split()
        sticker.append([int(l) for l in line])
    stickers.append(sticker)

# print(stickers)

def put(x, y, sticker):
    n, m = len(sticker), len(sticker[0])
    for i in range(n):
        for j in range(m):
            notebook[x + i][y + j] += sticker[i][j]

def can_apply_sticker(sticker, x, y):
    n = len(sticker)      # sticker의 행 개수
    m = len(sticker[0])   # sticker의 열 개수

    # notebook의 (x, y) 위치에서 (x+n, y+m) 범위가 sticker와 겹치는지 확인
    for i in range(n):
        for j in range(m):
            if notebook[x + i][y + j] & sticker[i][j]:
                return False
    return True

def check(sticker):
    n, m = len(sticker), len(sticker[0])
    if n > N or m > M:
        return (-1, -1)
    
    for i in range(N-n+1):
        # start_row = i
        for j in range(M-m+1):
            # start_col = j
            if can_apply_sticker(sticker, i, j):
                return (i, j)
            
    return (-1, -1)
            
def rotate(sticker):#, k):
    n, m = len(sticker), len(sticker[0])
    new_sticker = [[0 for _ in range(n)] for _ in range(m)]


    for i in range(n):
        for j in range(m):
            if sticker[i][j]:     
                #if k == 0:
                new_sticker[j][n-i-1] = 1
                # elif k == 1:
                #     new_sticker[j][] = 1
                # elif k == 2:
                #     new_sticker[j][] = 1
                # else:
                #     pass

    return new_sticker

for sticker in stickers:
    for k in range(4):
        i, j = check(sticker)
        if i != -1 and j != -1:
            put(i, j, sticker)
            break
        sticker = rotate(sticker)#, k)

count = 0
for line in notebook:
    count += line.count(1)

print(count)