# 4
# 1 1 5 31
# 1 1 6 30
# 5 15 8 31
# 6 10 12 10

# -> 2

N = int(input())
count = 0

flowers = []
for _ in range(N):
    flower = list(map(int, input().split()))
    if flower[2] < 3 or (flower[2] == 3 and flower[3] == 1):
        continue
    elif flower[0] > 11:
        continue
    flowers.append(flower)

flowers.sort(key = lambda x : (-x[2], -x[3], x[0], x[1]))

#print(flowers)

if flowers[0][2] < 12:
    print(count)

else:
    i = 0
    index = 0
    min_start = (flowers[0][0], flowers[0][1])
    while i < len(flowers) and flowers[i][2] > 11:
        if min_start[0] > flowers[i][0] or (min_start[0] == flowers[i][0] and min_start[1] >= flowers[i][1]):     
            min_start = (flowers[i][0], flowers[i][1])
            index = i
        i += 1
    i = index
    
    #print(index)

    while i < len(flowers):
        count += 1
        cur_f = flowers[i]

        #print(cur_f)

        # 선택된 꽃이 3/1일이나 그 이전에 핀 경우 종료
        if cur_f[0] < 3 or (cur_f[0] == 3 and cur_f[1] == 1):
            print(count)
            break

        j = i+1
        # 현재 꽃의 시작을 저장
        min_start = (cur_f[0], cur_f[1])

        # 다음 꽃을 탐색
        while j < len(flowers) and (cur_f[0] < flowers[j][2] or (cur_f[0] == flowers[j][2] and cur_f[1] <= flowers[j][3])):
            if min_start[0] > flowers[j][0] or (min_start[0] == flowers[j][0] and min_start[1] >= flowers[j][1]):
                min_start = (flowers[j][0], flowers[j][1])
                index = j
            j += 1
        i = index

        # 만약 다음 꽃을 적절히 발견 못했다면
        if min_start == (cur_f[0], cur_f[1]):
            print(0)
            break

