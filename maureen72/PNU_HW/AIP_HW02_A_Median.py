
lst = eval(input("Enter measurements as a list: ")) # 리스트 입력받기
lst.sort() # 오름차순 정렬

length = len(lst)

median = 0 # 초기 값 설정

if(length % 2 == 1) : # odd이면 -> 중간값
    median = lst[length // 2]
else : # even이면 -> 중간에 있는 값 두 개의 평균
    median = (lst[length // 2 - 1] + lst[length // 2]) / 2

print("Median: {}".format(median))