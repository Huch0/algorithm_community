class Solution:
    def TwoCaps(self, file_name):
        #입력 처리
        infile = open(file_name, 'r')
        n = int(infile.readline())

        points = []
        for _ in range(n):
            line = infile.readline().split()
            point = (int(line[0]), int(line[1]))
            points.append(point)

        time = int(infile.readline())

        infile.close()

        #총 거리 계산
        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        total_distance = distance(points[-1], points[0])
        for i in range(len(points)-1):
            total_distance += distance(points[i], points[i+1])
        
        #충돌 지점 처리
        cap1 = points[0]
        cap2 = points[len(points)//2 - 1]

        # 방향 기저 벡터 반환
        def cal_direction(p1, p2):
            if (p1[0] - p2[0]) == 0 and p1[1] - p2[1] != 0:
                return (0, int((p2[1] - p1[1]) / abs(p2[1] - p1[1])))
            elif (p1[1] - p2[1]) == 0 and p1[0] - p2[0] != 0:
                return (int((p2[0] - p1[0]) / abs(p2[0] - p1[0])), 0)
            else:
                return (0, 0)

        def cal_point(start, duration, points):
            check = 0
            if start == cap1:
                for i in range(len(points)-1):
                    dist = distance(points[i+1], points[i])
                    if duration < dist:
                        check = i
                        break
                    duration -= dist
                dir_x , dir_y = cal_direction(points[check], points[check+1])
                return (points[check][0] + dir_x * duration, points[check][1] + dir_y * duration)
            elif start == cap2:
                for i in range(len(points)//2 - 1, len(points)):
                    dist = distance(points[i+1], points[i])
                    if duration < dist:
                        check = i
                        break
                    duration -= dist
                dir_x , dir_y = cal_direction(points[check], points[check+1])
                return (points[check][0] + dir_x * duration, points[check][1] + dir_y * duration)

        def cal_distance_between_c1_c2():
            # 정방향 계산
            dist = 0
            for i in range(len(points)//2 - 1):
                dist += distance(points[i+1], points[i])
            return dist
        
        crash_p1 = cal_point(cap1, cal_distance_between_c1_c2() / 2, points)
        crash_p2 = cal_point(cap2, (total_distance - cal_distance_between_c1_c2()) / 2, points)

        #방향과 시간 설정
        time = time % total_distance
        
        def is_between(p1, p2, test):
            if p1[0] == p2[0] == test[0]:
                return p1[1]<=test[1]<=p2[1] or p2[1]<=test[1]<=p1[1]
            elif p1[1] == p2[1] == test[1]:
                return p1[0]<=test[0]<=p2[0] or p2[0]<=test[0]<=p1[0]
            else:
                return False

        c1 = []
        c2 = []

        c1_runner = 0
        c1_direction = 1

        c2_runner = len(points)//2 - 1
        c2_direction = -1

        while True:
            if c1.count(cap1) > 2:
                break
            c1.append(points[c1_runner])
            c2.append(points[c2_runner])
            if is_between(points[c1_runner], points[c1_runner+1], crash_p1):
                if points[c1_runner] != crash_p1:
                    c1.append(crash_p1)
                    c1.append(points[c1_runner])
                    c2.append(crash_p1)
                    c2.append(points[c2_runner])
                c1_direction *= -1
                c2_direction *= -1
            elif is_between(points[c1_runner-1], points[c1_runner], crash_p2):
                if points[c1_runner] != crash_p2:
                    c1.append(crash_p2)
                    c1.append(points[c1_runner])
                    c2.append(crash_p2)
                    c2.append(points[c2_runner])
                c1_direction *= -1
                c2_direction *= -1
            c1_runner += c1_direction
            c2_runner += c2_direction
                
        def cal_result(points, time):
            cal_time = time
            check = 0
            for i in range(len(points) - 1):
                dist = distance(points[i+1], points[i])
                if dist > cal_time:
                    check = i
                    break
                cal_time -= dist
            dir_x, dir_y = cal_direction(points[check], points[check+1])
            return ( int(points[check][0] + dir_x * cal_time), int(points[check][1] + dir_y * cal_time))
        
        return [cal_result(c1, time), cal_result(c2, time)]

### TEST CODE
if __name__ == "__main__":
    s = Solution()
    for i in range(1, 10):
        input_file_name = "Cho-4-Test/0" + str(i) + ".inp"
        result_file_name = "Cho-4-Test/0" + str(i) + ".out"

        infile = open(result_file_name, "r")
        
        results = []
        for point in s.TwoCaps(input_file_name):
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
        input_file_name = "Cho-4-Test/" + str(i) + ".inp"
        result_file_name = "Cho-4-Test/" + str(i) + ".out"

        infile = open(result_file_name, "r")
        
        results = []
        for point in s.TwoCaps(input_file_name):
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