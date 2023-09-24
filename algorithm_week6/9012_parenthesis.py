num = int(input())
linelist = []
for _ in range(num):
    line = input()
    linelist.append(line)

for line in linelist:
    stack = []
    for char in line:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if stack:
                stack.pop()
            else: 
                print('NO')
                break
    else: # break와 쌍을 이뤄 break되지 않았다면 이라는 의미
        if not stack:
            print("YES")
        else:
            print("NO")