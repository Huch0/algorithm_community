def populateDictionary():
    #단위가 적힌 파일 열기
    infile = open('Units.txt', 'r')
    unitDic = {} # 빈 딕셔너리 생성(조건에서 dictionary operation을 사용하라고 했으므로)

    for line in infile :
        #한줄을 읽어서 ,를 기준으로 단위와 값으로 변환
        (unit, value) = line.split(',') 
        unitDic[unit] = float(value) # 이를 딕셔너리에 추가
    return unitDic

def getInput():
    #변환하고자하는 단위와 길이, 그리고 변환결과 단위 입력받기
    orig = input("Unit to convert from: ")
    dest = input("Unit to convert to: ")
    length = int(input("Enter length in {}: ".format(orig)))
    return (orig, dest, length)
    
def main(): # 주어진 skeleton code
    feet = populateDictionary() 
    orig, dest, length = getInput() 
    ans = length * feet[orig] / feet[dest] 
    print("Length in {0}: {1:,.4f}".format(dest, ans))
    
main()

