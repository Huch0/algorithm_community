### 문제 이해
# 1. 각 입력에 따른 Disk 처리 알고리즘 구현
# 2. 입력 처리
# 3. 결과 반환

class Solution:
    def Disk(self, file_name):
        disk = []
        results = []

        infile = open(file_name, "r")
        V = int(infile.readline().rstrip())

        # 1번을 위한 보조 함수
        # 디스크 내부의 빈 공간을 반환함
        def check_free_space():
            free_space = []
            
            start_point = 0
            for i in range(len(disk)):
                if start_point != disk[i][1]:
                    free_space.append((start_point, disk[i][1]))
                start_point = disk[i][2]

            if start_point != V:
                free_space.append((start_point, V))

            return free_space
            
                
        # 1. 각 입력에 따른 Disk 처리 알고리즘
        def DiskAlgorithm(command, filename = None, size = None):
            if command == "write":
                # 이미 같은 이름의 파일이 존재하는 경우
                for i in range(len(disk)):
                    if disk[i][0] == filename:
                        return "error"

                free_space = check_free_space()
                selected_space = -1
                free_sum = 0
                for i in range(len(free_space)):
                    free_sum += free_space[i][1] - free_space[i][0]
                    if free_space[i][1] - free_space[i][0] >= size:
                        selected_space = i
                        break
                
                # 공간이 파일 크기보다 적게 남아있을 경우
                if free_sum < size:
                    return "diskfull"
                # 빈 공간의 집합에 파일 크기보다 큰 공간이 있을 경우
                if selected_space >= 0:
                    disk.append([filename, free_space[selected_space][0], free_space[selected_space][0] + size])
                # 잘게 쪼개서 저장해야 할 경우
                else:
                    for space in free_space:
                        if size <= (space[1] - space[0]):
                            disk.append([filename, space[0], space[0]+size])
                            break                        
                        size -= (space[1] - space[0])
                        disk.append([filename, space[0], space[1]])
                return None

            elif command == "delete":
                count = 0
                for i in range(len(disk)):
                    if disk[i][0] == filename:
                        count += 1
                if count == 0:
                    return "error"
                for i in range(len(disk)):
                    if count == 0:
                        return None
                    if disk[i][0] == filename:
                        disk.remove(disk[i])
                        count -= 1

            elif command == "show":
                result = []
 
                for i in range(len(disk)):
                    if disk[i][0] == filename:
                        result.append(str(disk[i][1]))
                        
                if len(result) == 0:
                    return "error"
                
                return result

            else:
                start_point = 0
                for i in range(len(disk)):
                    distance = disk[i][1] - start_point
                    if distance != 0:
                        disk[i][1] -= distance
                        disk[i][2] -= distance
                    start_point = disk[i][2]

                remove_target = []
                for i in range(len(disk)-1):
                    starting_point = i
                    while disk[i][0] == disk[i+1][0]:
                        i += 1
                        remove_target.append(i)
                        if i == len(disk)-1:
                            break
                    if starting_point != i:
                        disk[starting_point][2] = disk[i][2]
                for rm in remove_target:
                    disk.remove(disk[rm])

            return None


        for line in infile:
            if line == "end":
                break
            line = line.split()
            if len(line) == 1:
                result = DiskAlgorithm("Compact")
            elif len(line) == 2:
                result = DiskAlgorithm(line[0], line[1])
            else:
                result = DiskAlgorithm(line[0], line[1], int(line[2]))
            print(disk)
            if result != None:
                results.append(result)

        infile.close()

        return results


### TEST CODE
if __name__ == "__main__":
    s = Solution()
    print(s.Disk("Cho-12-Test/02.inp"))
    # for i in range(1, 10):
    #     input_file_name = "Cho-12-Test/0" + str(i) + ".inp"
    #     result_file_name = "Cho-12-Test/0" + str(i) + ".out"
        
    #     infile = open(result_file_name, "r")
        
    #     results = s.Disk(input_file_name)

    #     outputs = []
        
    #     for line in infile:
    #         outputs.append(line.split())

    #     infile.close()
    #     if results == outputs:
    #         print("CORRECT")
    #     else:
    #         print("INCORRECT")
    
    # for i in range(10, 16):
    #     input_file_name = "Cho-12-Test/" + str(i) + ".inp"
    #     result_file_name = "Cho-12-Test/" + str(i) + ".out"

    #     infile = open(result_file_name, "r")
        
    #     results = s.Disk(input_file_name)

    #     outputs = []
        
    #     for line in infile:
    #         line = [int(num) for num in line.split()]
    #         outputs.append(line)

    #     infile.close()
    #     if results == outputs:
    #         print("CORRECT")
    #     else:
    #         print("INCORRECT")