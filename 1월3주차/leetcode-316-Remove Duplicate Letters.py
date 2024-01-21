class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for _ in range(len(temperatures))]
        mystack = []
        mystack.append(temperatures[0])
        
        for i in range(1, len(temperatures)):
            r = 1
            while(mystack[-r] < temperatures[i]):  # mystack이 비어있는 경우는 없음. 무조건 1개는 들어가 있음
                if answer[i-r] == 0:
                    answer[i - r] = r
                if len(mystack) == r:
                    mystack.clear()
                    break
                r = r+1
            mystack.append(temperatures[i])

        return answer