class Solution:
    def Robocap(self, file_name):
        # 입력 처리
        infile = open(file_name, "r")
        n = int(infile.readline().rstrip())

        points = []

        for _ in range(n):
            line = infile.readline()
            line = line.split()
            points.append((int(line[0]), int(line[1])))            

        line = infile.readline()
        tests = [int(i) for i in line.split()]

        # 수직, 수평 거리 측정
        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        distances = []
        for i in range(len(points)):
            if i == len(points)-1:
                distances.append(distance(points[i], points[0]))
                break
            distances.append(distance(points[i], points[i+1]))
        
        total_distance = sum(distances)

        tests = [test % total_distance for test in tests]
        
        # 방향 기저 벡터 반환
        def direction(p1, p2):
            if (p1[0] - p2[0]) == 0 and p1[1] - p2[1] != 0:
                return (0, int((p2[1] - p1[1]) / abs(p2[1] - p1[1])))
            elif (p1[1] - p2[1]) == 0 and p1[0] - p2[0] != 0:
                return (int((p2[0] - p1[0]) / abs(p2[0] - p1[0])), 0)
            else:
                return (0, 0)

        result = []
        # 구간 파악
        for test in tests:
            i = 0
            while test > distances[i]:
                test -= distances[i]
                i += 1
            
            if i != len(points)-1:
                dir_x, dir_y = direction(points[i], points[i+1])
            else:
                dir_x, dir_y = direction(points[i], points[0])

            result.append(((dir_x * test) + points[i][0], (dir_y * test) + points[i][1]))
        
        return result

### TEST CODE 
if __name__ == "__main__":
    s = Solution()
    for i in range(1, 10):
        input_file_name = "Cho-3-Test/0" + str(i) + ".inp"
        result_file_name = "Cho-3-Test/0" + str(i) + ".out"

        infile = open(result_file_name, "r")
        
        results = []
        for point in s.Robocap(input_file_name):
            results.append(point)
        
        outputs = []
        
        for line in infile:
            line = line.split()
            x, y = int(line[0]), int(line[1])
            outputs.append((x, y))

        infile.close()

        if results == outputs:
            print("CORRECT")
        else:
            print("INCORRECT")
    
    for i in range(10, 13):
        input_file_name = "Cho-3-Test/" + str(i) + ".inp"
        result_file_name = "Cho-3-Test/" + str(i) + ".out"

        infile = open(result_file_name, "r")
        
        results = []
        for point in s.Robocap(input_file_name):
            results.append(point)
        
        outputs = []
        
        for line in infile:
            line = line.split()
            x, y = int(line[0]), int(line[1])
            outputs.append((x, y))

        infile.close()

        if results == outputs:
            print("CORRECT")
        else:
            print("INCORRECT")