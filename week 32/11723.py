import sys

N = int(sys.stdin.readline())

mySet=set()
for _ in range(N):
    command, num=sys.stdin.readline().split()
    num=int(num)
    if command == "add":
        mySet.add(num)
    elif command == "remove":
        mySet.discard(num)
    elif command == "check":
        if num in mySet:
            print(1)
        else:
            print(0)
    elif command=="toggle":
        if num in mySet:
            mySet.discard(num)
        else:
            mySet.add(num)
    elif command=="all":
        mySet={range(1,21)}
    else:
        mySet=set()