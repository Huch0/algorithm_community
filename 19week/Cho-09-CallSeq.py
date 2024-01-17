### 문제 이해
#1. 입력 처리
#2. Act, Func 스택 구현
#3. 결과 처리

from collections import defaultdict

class Solution:
    def CallSeq(self, file_name):

        #1. 입력 처리
        program = defaultdict(list)
        
        infile = open(file_name, 'r')
        first_line = infile.readline().split()
        K1, K2 = int(first_line[1]), int(first_line[2])

        for line in infile:
            line = line.split()
            program[line[0]] = line[1:]

        # 총 수행문 길이 구하기
        count_act = 0

        for function in program:
            for statement in program[function]:
                if 'a' <= statement[0] <= 'z' or '0' <= statement[0] <= '9':
                    count_act += 1

        #2. 스택 구조로 결과 처리 함수 구현
        def get_result(K):
            functions = ['M']
            runner = ''
            index = defaultdict(int)

            for function in program:
                index[function] = 0

            acts = []
            
            i = 0
            noneflag = False

            while True:
                if len(acts) == K:
                    break
                if len(functions) == 0:
                    if K > 0:
                        noneflag = True
                    break

                active_function = functions[-1]
                runner = program[active_function][index[active_function]]
                
                if 'A' <= runner <= 'Z':
                    if runner in functions:
                        return "DEADLOCK"
                    index[active_function] += 1
                    functions.append(runner)
                    
                elif runner == '$':
                    index[active_function] = 0
                    functions.pop()
                
                else:
                    index[active_function] += 1
                    acts.append(runner)
                
                i += 1
            
            #print(K, len(acts))

            if noneflag:
                return "NONE"
            if K < 0:
                
                return get_result(len(acts) + K + 1)
            else:
                return functions[-1] + '-' + acts[-1]
            
        # 3. 결과 처리
        if get_result(99999999) == "DEADLOCK":
            return ["DEADLOCK"]
        return [get_result(K1), get_result(K2)]
            
### TEST CODE
if __name__ == "__main__":
    s = Solution()
    #print(s.CallSeq("Cho-9-Test/09.inp"))
    for i in range(1, 10):
        input_file_name = "Cho-9-Test/0" + str(i) + ".inp"
        result_file_name = "Cho-9-Test/0" + str(i) + ".out"

        infile = open(result_file_name, "r")
        
        results = s.CallSeq(input_file_name)

        outputs = []
        
        for line in infile:
            outputs.append(line.rstrip())

        infile.close()
        if results == outputs:
            print("CORRECT")
        else:
            print("INCORRECT")
    
    for i in range(10, 16):
        input_file_name = "Cho-9-Test/" + str(i) + ".inp"
        result_file_name = "Cho-9-Test/" + str(i) + ".out"

        infile = open(result_file_name, "r")
        
        results = s.CallSeq(input_file_name)

        outputs = []
        
        for line in infile:
            outputs.append(line.rstrip())

        infile.close()

        if results == outputs:
            print("CORRECT")
        else:
            print("INCORRECT")