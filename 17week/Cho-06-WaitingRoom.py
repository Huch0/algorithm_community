from collections import defaultdict

class Solution:
    def WaitingRoom(self, file_name):
        #입력 처리
        infile = open(file_name, 'r')
        test = infile.readline().split()

        N, k = int(test[0]), int(test[1])

        waiting_list = []

        for line in infile:
            costomer = line.rstrip()
            if costomer[0] == '-' and ('+' + costomer[1:]) not in waiting_list:
                continue
            waiting_list.append(costomer)

        # plus_count = 0
        # minus_count = 0
        # for i in range(len(waiting_list)):
        #     if waiting_list[i][0] == '+':
        #         plus_count += 1
        #     else:
        #         minus_count += 1

        # print("plus count is ", plus_count)
        # print("minus count is ", minus_count)

        #딕셔너리 구조 생성
        wait_dict = defaultdict(list)

        for i in range(N):
            wait_dict[i] # 이렇게 하면 defaultdict가 빈 리스트를 할당합니다.

        # 저장 알고리즘
        ### 1. i th가 비어있거나 i+1 th가 비어있을 떄
        ### 2. target < i+1 th min
        ### 3. i th min < target < i th Max
        # count = 0
        for query in waiting_list:
        #     if count % 10 == 0:
        #         for i in range(N):
        #             if not wait_dict[i]:
        #                 break
        #             print(wait_dict[i], end= " ")
        #         print()

            #count += 1
            target = int(query[2:])
            split_state = (False, -1)
            # query가 +로 시작하는 경우
            if query[0] == '+':
                for i in range(N):
                    if not wait_dict[i] or not wait_dict[i+1] or wait_dict[i][0] < target < wait_dict[i][-1] or target < wait_dict[i+1][0]:
                        wait_dict[i].append(target)
                        wait_dict[i].sort()
                        if len(wait_dict[i]) == 2*k:
                            split_state = (True, i)
                        break
            # query가 -로 시작하는 경우
            elif query[0] == '-':
                for i in range(N):
                    if target in wait_dict[i]:
                        wait_dict[i].remove(target)
                        if not wait_dict[i]:
                            while wait_dict[i+1]:
                                wait_dict[i] = wait_dict[i+1][:]
                                i += 1
                            wait_dict[i] = []
                        break

            # split 수행
            if split_state[0]:
                index = split_state[1]
                split_list = wait_dict[index][k:]
                wait_dict[index] = wait_dict[index][:k]

                i = split_state[1]

                if wait_dict[i+1]:
                    while wait_dict[i+1]:
                        i += 1
                    i += 1
                    while i > (index+1):
                        wait_dict[i] = wait_dict[i-1][:]
                        i -= 1
                
                wait_dict[index+1] = split_list
            
        # 결과 출력
        result = []
        for i in range(N):
            if not wait_dict[i]:
                break
            result.append(wait_dict[i][0])

        return result

### TEST CODE
if __name__ == "__main__":
    s = Solution()
    #print(s.WaitingRoom("Cho-6-Test/02.inp"))
    for i in range(1, 10):
        input_file_name = "Cho-6-Test/0" + str(i) + ".inp"
        result_file_name = "Cho-6-Test/0" + str(i) + ".out"

        infile = open(result_file_name, "r")
        
        results = s.WaitingRoom(input_file_name)

        outputs = []
        
        for line in infile:
            line = line.rstrip()
            outputs.append(int(line))

        infile.close()

        if results == outputs:
            print("CORRECT")
        else:
            print("INCORRECT")
    
    for i in range(10, 16):
        input_file_name = "Cho-6-Test/" + str(i) + ".inp"
        result_file_name = "Cho-6-Test/" + str(i) + ".out"

        infile = open(result_file_name, "r")
        
        results = s.WaitingRoom(input_file_name)
        
        outputs = []
        
        for line in infile:
            line = line.rstrip()
            outputs.append(int(line))

        infile.close()

        if results == outputs:
            print("CORRECT")
        else:
            print("INCORRECT")