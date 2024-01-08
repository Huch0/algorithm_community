### 문제 이해
#1. 입력 처리
#2. 컨테이너 높이를 담은 리스트 생성
#3. 가장 높은 곳 찾기, 무게가 클 수록 우선순위
#4. 가장 낮은 곳 찾기, 앞에 있을 수록 우선순위
#5. 옮기기
#6. 사후 처리
#7. 위 과정 반복 & 결과 출력

class Solution:
    def Yard(self, file_name):
        #1. 입력 처리
        infile = open(file_name, 'r')
        
        N = int(infile.readline().rstrip())

        containers = []
        #2. 컨테이너 높이를 담을 리스트 생성
        heights = []

        for line in infile:
            line = [int(container) for container in line.split()]
            containers.append(line[1:])
            heights.append(line[0])

        #3. 가장 높은 곳 잡기
        def get_target():
            max_height = max(heights)
            max_container = 0
            target = 0
            
            for i in range(len(heights)):
                if heights[i] == max_height and max_container < containers[i][-1]:
                    max_container = containers[i][-1]
                    target = i

            return target
        
        #4. 가장 낮은 곳 찾기
        def get_location():
            min_height = min(heights)
            target = 0

            for i in range(len(heights)):
                if heights[i] == min_height:
                    return i
                
        #5. 옮기기
        def move(target, location):
            container = containers[target].pop()
            containers[location].append(container)
            heights[target] -= 1
            heights[location] += 1

        #6. 반복문 수행 및 사후 처리
        while max(heights) - min(heights) != 1:
            move(get_target(), get_location())

        #7. 결과 출력
        for i in range(len(containers)):
            if not containers[i]:
                containers[i] = [0]

        return containers



### TEST CODE
if __name__ == "__main__":
    s = Solution()
    for i in range(1, 10):
        input_file_name = "Cho-8-Test/0" + str(i) + ".inp"
        result_file_name = "Cho-8-Test/0" + str(i) + ".out"

        infile = open(result_file_name, "r")
        
        results = s.Yard(input_file_name)

        outputs = []
        
        for line in infile:
            line = [int(container) for container in line.split()]
            outputs.append(line)

        infile.close()

        if results == outputs:
            print("CORRECT")
        else:
            print("INCORRECT")
    
    for i in range(10, 16):
        input_file_name = "Cho-8-Test/" + str(i) + ".inp"
        result_file_name = "Cho-8-Test/" + str(i) + ".out"

        infile = open(result_file_name, "r")
        
        results = s.Yard(input_file_name)
        
        outputs = []
        
        for line in infile:
            line = [int(container) for container in line.split()]
            outputs.append(line)

        infile.close()

        if results == outputs:
            print("CORRECT")
        else:
            print("INCORRECT")