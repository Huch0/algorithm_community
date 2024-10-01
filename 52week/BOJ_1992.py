# 8
# 11110000
# 11110000
# 00011100
# 00011100
# 11110000
# 11110000
# 11110011
# 11110011

# -> ((110(0101))(0010)1(0001))

N = int(input())
video = []

for _ in range(N):
    line = input()
    line = [int(i) for i in line]
    video.append(line)

def check_eq(x, y, n):
    first = video[x][y]

    for i in range(n):
        for j in range(n):
            if video[x+i][y+j] != first:
                return False
    return True

def func(x, y, n):

    if check_eq(x, y, n):
        return str(video[x][y])

    result = "("
    
    m = n//2
    
    for i in range(2):
        for j in range(2):
            if check_eq(x + m*i, y + m*j, m):
                result += str(video[x+m*i][y+m*j])
            else:
                result += func(x + m*i, y + m*j, m)
    
    result += ")"
    return result

print(func(0, 0, N))