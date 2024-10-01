import os

def main():
    mySet = readSetFromFile()
    name = inputName()
    modifiedSet = insertSet(mySet, name)
    writeToFile(modifiedSet)

def readSetFromFile():
    if os.path.isfile("Names.txt"):  # 파일이 존재하는지 확인
        infile = open("Names.txt", "r")  # 파일 열기
        namesSet = {line.strip() for line in infile}  # 파일에서 한 줄씩 읽고 set에 추가 (공백 제거)
        infile.close()  # 파일 닫기
        return namesSet  # set 반환 (정렬되지 않은 상태)
    else:  # 파일이 없으면
        print("Names.txt does not exist.\nTerminate program.")
        exit(1)  # 프로그램 종료


def inputName():
    name = input("Enter a first name to be included: ")  # 이름 입력받기
    return name

def insertSet(mySet, name):
    if name in mySet:  # 이름이 set에 있으면
        print(f"{name} is already in Names.txt")  # 이미 있다고 출력
    else:  # 이름이 set에 없으면
        mySet.add(name)  # set에 추가하고
        print(f"{name} is added in Names.txt")  # 추가했다고 출력
    return mySet  # 변경된 set 반환

def writeToFile(modifiedSet):
    sorted_list = sorted(modifiedSet)  # set을 정렬된 리스트로 변환
    with open("Names.txt", "w") as Names_txt:  # 파일 쓰기 모드로 열기
        for i in sorted_list:  # 정렬된 리스트에서 한 항목씩 가져오기
            Names_txt.write(i + "\n")  # 파일에 작성 및 줄바꿈

main()
