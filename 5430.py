times=int(input())

for _ in range(times):
    func = input()
    n=int(input())
    arr= eval(input())
    error=0
    rCount=0
    for c in func:
        if c=='R':
            rCount+=1
        elif c=='D':
            if len(arr)<1:
                error=1
                break
            else:
                if rCount%2==0:
                    arr.pop(0)
                else:
                    arr.pop()
    if not error:
            if rCount%2:
                arr.reverse()
            print(f"[{','.join(map(str, arr))}]")
    else:
        print("error")