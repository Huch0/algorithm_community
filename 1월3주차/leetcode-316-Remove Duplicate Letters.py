# 처음 풀이
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
    
# 필요한 것만 확인하면 되는, 개선된 풀이
class Solution:
    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        answer = [0 for _ in range(len(temperatures))]
        mystack = []
        mystack.append(0)
        for i in range(1, len(temperatures)):
            while temperatures[mystack[-1]] < temperatures[i]: # mystack에는 최소 원소 1개는 존재함
                answer[mystack[-1]] = i - mystack[-1]
                mystack.pop()
                if len(mystack) == 0:
                    break
            mystack.append(i)
        return answer