count = 1
consider = True
stc = []
op = []

N = int(input())
for i in range(N):
    num = int(input())

    while count <= num:

        stc.append(count)
        op.append('+')
        count += 1


    if stc[-1] == num:
        stc.pop()
        op.append('-')

    else:
        consider = False
        break


if consider == False:
    print("NO")
else:
    for i in op:
        print(i)