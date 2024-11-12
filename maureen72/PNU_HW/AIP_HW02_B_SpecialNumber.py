for num in range(10000, 100000): # 10000~99999 사이의 수
    #전체적인 흐름 : 숫자를 문자열로 변환 -> 문자열을 리스트로 변환 -> 리스트를 역순으로 정렬 -> 리스트의 원소들로 문자열 만들기
    numStr = str(num) # 숫자를 문자열로 변환
    lst = []
    for i in numStr: # 문자열을 리스트로 변환
        lst.append(i) 
    lst.reverse() # 리스트를 역순으로 정렬
    newNum = int("".join(lst)) # 리스트의 원소들로 문자열 만들기

    if(num*4 == newNum):
        print("Since 4 * {} is {},\nThe special number is {}.".format(num, newNum, newNum))
