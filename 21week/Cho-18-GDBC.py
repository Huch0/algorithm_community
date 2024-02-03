### 문제 이해
# 1. 입력 처리: R의 경우 각 입력을 딕셔너리 구조로 저장
# key 를 유전자 set (Tuple 형태의)으로, value를 질병 코드로
# Q의 경우 딕셔너리 조회 후 반환

from collections import defaultdict

class Solution:
    def GDBC(self, file_name):
        # 1. 입력 처리
        infile = open(file_name, "r")

        server = defaultdict(list)
        outputs = []

        while True:
            line = infile.readline().split()
            if len(line) == 1:
                break
            gene = tuple(sorted(line[1:-1]))
            if line[0] == "R":    
                server[gene].append(line[-1])
                
            else:
                if server[gene] == []:
                    outputs.append(['None'])
                    continue
                output = [disease for disease in server[gene]]
                output.sort(key = lambda x : -int(x))
                outputs.append(output)

        infile.close()
        
        return outputs

### TEST CODE
if __name__ == "__main__":
    s = Solution()
    #print(s.GDBC("Cho-18-Test/12.inp"))
    for i in range(1, 10):
        input_file_name = "Cho-18-Test/0" + str(i) + ".inp"
        result_file_name = "Cho-18-Test/0" + str(i) + ".out"
        
        infile = open(result_file_name, "r")
        
        results = s.GDBC(input_file_name)

        outputs = []
        for line in infile:
            outputs.append(line.split())

        #print(outputs)
        infile.close()
        if results == outputs:
            print("CORRECT")
        else:
            print("INCORRECT")
    
    for i in range(10, 16):
        input_file_name = "Cho-18-Test/" + str(i) + ".inp"
        result_file_name = "Cho-18-Test/" + str(i) + ".out"

        infile = open(result_file_name, "r")
        
        results = s.GDBC(input_file_name)

        outputs = []
        for line in infile:
            outputs.append(line.split())

        infile.close()
        if results == outputs:
            print("CORRECT")
        else:
            print("INCORRECT")