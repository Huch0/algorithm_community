#입력 처리
#총 인원 수를 입력받는다
#각각의 이름과 입찰가를 입력받는다.
#해당 자료를 튜플 구조로 저장한다.
class Solution:
    def Bidding(self, file_name):

        input_file = open(file_name, "r")

        input_file.readline()

        biddings = []

        for line in input_file:
            line = line.split()
            biddings.append((line[0], int(line[1])))

        input_file.close()

        #최고가 입찰자 계산
        biddings.sort(key = lambda x : x[1], reverse=True)

        if len(biddings) == 1 or biddings[0][1] != biddings[1][1]:
            return biddings[0][0]
        #출력 처리
        for i in range(len(biddings)-1):

            if biddings[i][1] != biddings[i+1][1]:
                if i != len(biddings)-2 and biddings[i+1][1] == biddings[i+2][1]:
                    continue
                else:
                    return biddings[i+1][0]
            # if biddings[i][1] == biddings[i+1][1]:
            #     continue
            # elif i != len(biddings)-2 and biddings[i+1][1] != biddings[i+2][1]:
            #     return 
        return "NONE"
        
### TEST CASE
# Cho-1-Test 폴더에 들어있는 *.inp을 입력으로 하고 *.out을 출력과 비교한다

### TEST CODE 
if __name__ == "__main__":
    s = Solution()
    for i in range(1, 10):
        input_file_name = "Cho-1-Test/0" + str(i) + ".inp"
        result_file_name = "Cho-1-Test/0" + str(i) + ".out"

        infile = open(result_file_name, "r")
        
        if s.Bidding(input_file_name) == infile.readline().strip():
            print("CORRECT")
        else:
            print("INCORRECT")
        
        infile.close()
    
    for i in range(10, 13):
        input_file_name = "Cho-1-Test/" + str(i) + ".inp"
        result_file_name = "Cho-1-Test/" + str(i) + ".out"

        infile = open(result_file_name, "r")
        
        if s.Bidding(input_file_name) == infile.readline().strip():
            print("CORRECT")
        else:
            print("INCORRECT")
        
        infile.close()

    #print(s.Bidding("Cho-1-Test/03.inp"))