class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        days = [0 for i in range(len(temperatures))]

        for index, temp in enumerate(temperatures):
            #더 작거나 같은 온도인 경우만 스택에 쌓는다
            if len(stack) == 0 or stack[-1] >= temp:
                stack.append(temp)
                continue
            
            count = 0

            #더 높은 온도를 마주하면 스택에서 지우고
            while stack[-1] < temp:
                stack.pop()
                count += 1
                #days의 값이 0이면 수정
                while days[index - count] != 0:
                    count += 1
                
                #days 리스트의 값을 수정
                days[index - count] = count

            stack.append(temp)

        return days