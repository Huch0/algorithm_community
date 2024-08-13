n = int(input())

n_beatiful_nums = 0


def beautiful_num(num):
    global n_beatiful_nums

    if len(num) == n:
        n_beatiful_nums += 1
        return
    elif len(num) > n:
        return

    for i in range(1, 5):
        beautiful_num(num + str(i) * i)


beautiful_num('')
print(n_beatiful_nums)
