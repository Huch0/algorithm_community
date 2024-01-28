### 문제 이해
# 1. 입력 처리 : 방문자 정보를 객체로 저장해둔다
# 2. User 클래스에 비교 연산 메소드를 구현해둔다
# 3. 차례대로 시간 조건이 부합하면 대기실(priority Queue)에 넣는다
# 4. 상담 알고리즘을 구현한다.

import heapq

class User:
    def __init__(self, visit_time, ID, remaining_time):
        self.ID = ID
        self.remaining_time = remaining_time
        self.visit_time = visit_time
        self.done = False

    # __lt__ 메서드를 정의하여 비교 기준을 설정
    def __lt__(self, other):
        # 남은 상담시간이 많은 것이 높은 우선순위를 가짐
        if self.remaining_time != other.remaining_time:
            return self.remaining_time > other.remaining_time
        # 남은 상담시간이 같으면 방문 시간이 빠른 것이 높은 우선순위를 가짐
        return self.visit_time < other.visit_time

class Solution:
    def Support(self, file_name):    

        # 1. 입력처리
        infile = open(file_name, "r")
        N = int(infile.readline())

        users = []

        for line in infile:
            line = line.split()
            users.append(User(int(line[0]), line[1], int(line[2])))

        infile.close()

        # 2. 대기실

        waiting = []
        set_time = 30

        outputs = []

        def visit_update(time):
            if not users:
                return

            selected_user = []
            for user in users:
                if user.visit_time <= time:
                    heapq.heappush(waiting, user)
                    selected_user.append(user)

            for sel_user in selected_user:
                users.remove(sel_user)

            #print(len(users))

        def counsil(time):
            if waiting:
                selected_user = heapq.heappop(waiting)
            else:
                min_visit_time = 9999999
                for user in users:
                    min_visit_time = min(user.visit_time, min_visit_time)
                return min_visit_time

            counsil_time = 0
            if selected_user.remaining_time <= 10:
                counsil_time = selected_user.remaining_time
                selected_user.remaining_time = 0
                selected_user.done = True
                #print(selected_user.ID)
                outputs.append(selected_user.ID)
            else:
                counsil_time = selected_user.remaining_time // 2
                selected_user.remaining_time -= counsil_time
                selected_user.visit_time = time + counsil_time
                heapq.heappush(waiting, selected_user)

            time += counsil_time
            return time

        current_time = set_time
        while len(outputs) < N:
            #print(current_time)
            visit_update(current_time)
            after_time = counsil(current_time)
            # if current_time > 1400:
            #     for user in waiting:
            #         print("user ID : ", user.ID, " user remaining_time : ", user.remaining_time)
            current_time = after_time

            
        return outputs


### TEST CODE
if __name__ == "__main__":
    s = Solution()
    #print(s.Support("Cho-14-Test/01.inp"))
    for i in range(1, 10):
        input_file_name = "Cho-14-Test/0" + str(i) + ".inp"
        result_file_name = "Cho-14-Test/0" + str(i) + ".out"
        
        infile = open(result_file_name, "r")
        
        results = s.Support(input_file_name)

        outputs = []
        
        for line in infile:
            outputs.append(line.rstrip())

        infile.close()
        if results == outputs:
            print("CORRECT")
        else:
            print("INCORRECT")
    
    for i in range(10, 16):
        input_file_name = "Cho-14-Test/" + str(i) + ".inp"
        result_file_name = "Cho-14-Test/" + str(i) + ".out"

        infile = open(result_file_name, "r")
        
        results = s.Support(input_file_name)

        outputs = []
        
        for line in infile:
            outputs.append(line.rstrip())

        infile.close()
        if results == outputs:
            print("CORRECT")
        else:
            print("INCORRECT")