class Solution:
    def Stairs(self, file_name):
        # 계단 입력처리
        infile = open(file_name, "r")
        stairs = [int(i) for i in infile.readline().split()]
        # 0은 버린다
        stairs.pop()

        # 계단 리스트의 정보를 이용해서 꼭짓점을 그린다.
        points = []

        x, y = 0, 0
        for i in range(0, len(stairs), 2):
            x += stairs[i]
            for j in range(i+1, len(stairs), 2):
                y += stairs[j]
            points.append((x, y))
            y = 0
        
        points.append((x, y))

        # print(points)

        # In, On, Out 판단
        test_points = []
        for line in infile:
            line = line.split()
            test_points.append((int(line[0]), int(line[1])))

        # print(test_points)

        def check(point):
            x = point[0]
            y = point[1]

            for i in range(len(points)-1):
                s_x = points[i][0]
                s_y = points[i][1]

                if x > s_x:
                    continue

                elif x == s_x:
                    next_y = points[i+1][1]
                    if next_y <= y <= s_y:
                        return "on"
                    elif s_y < y:
                        return "out"
                    elif y < next_y:
                        return "in"
                elif x < s_x:
                    if y == s_y:
                        return "on"
                    elif s_y < y:
                        return "out"
                    elif y < s_y:
                        return "in"
            return "out"
                
        # 출력 정리
        result = []
        for point in test_points:
            #print(check(point))
            result.append(check(point))
        
        infile.close()

        return ''.join(result)
    
### TEST CODE 
if __name__ == "__main__":
    s = Solution()

    for i in range(1, 10):
        input_file_name = "Cho-2-Test/0" + str(i) + ".inp"
        result_file_name = "Cho-2-Test/0" + str(i) + ".out"

        infile = open(result_file_name, "r")
        
        result = ''
        for line in infile:
            line = line.rstrip()
            result += line

        infile.close()

        if s.Stairs(input_file_name) == result:
            print("CORRECT")
        else:
            print("INCORRECT")
    
    for i in range(10, 13):
        input_file_name = "Cho-2-Test/" + str(i) + ".inp"
        result_file_name = "Cho-2-Test/" + str(i) + ".out"

        infile = open(result_file_name, "r")
        
        result = ''
        for line in infile:
            line = line.rstrip()
            result += line

        infile.close()

        if s.Stairs(input_file_name) == result:
            print("CORRECT")
        else:
            print("INCORRECT")
