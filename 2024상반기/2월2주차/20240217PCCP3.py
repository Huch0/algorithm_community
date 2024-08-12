# 틀린 이유 : c언어의 for문과 혼동해서
# for i in range(10) 이런식으로 쓰면 for문 안에서 i의 값을 임의로 바꿔도 다음 for문의 i값은 range함수가 만들어낸 값으로 들어간다

userinput = "-A-B"
t = 1
def backspace(s):
    while s[0] == "-":
        s = s[1:]
    i = len(s) - 1
    while i > 0: ### 틀린 부분, i의 값을 케이스에 맞게 조절하기 위해 for문이 아닌 while문 이용
        if s[i] == "-":
            if s[i-1] == "-":
                s = s[:i] + s[i+1:]
            else:
                s = s[:i-1] + s[i+1:] # 파이썬의 슬라이싱은 범위를 넘어가도 자동으로 처리해줌 (슬라이싱에서 out of range가 발생하진 않음)
                i = i-1
        i = i-1
    return s

def dfs(curindex, depth):
    if len(delayindex) == depth:
        mylist = [" " for x in range(len(userinput)*2 + 11)]
        for i in range(len(userinput)):
            mylist[i*2] = userinput[i]
        for n in delayindex:
            mylist[n*2 + t*2 + 1] = mylist[n*2]
            mylist[n*2] = " "
        mystr = ""
        for c in mylist:
            if c != " ":
                mystr = mystr + c
        possible.add(backspace(mystr))
    for i in range(curindex, len(userinput)):
        delayindex.append(i)
        dfs(i+1, depth)
        delayindex.pop()

possible = set()
delayindex = []
for i in range(0, len(userinput)+1):
    dfs(0, i)
print(sorted(possible))