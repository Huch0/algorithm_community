def dailyTemperatures(self, temperatures):
    stack = []
    result = [0] * len(temperatures)
    for i in range(len(temperatures)):
        if len(stack) == 0 or stack[-1] > temperatures[i]:
            stack.append(temperatures[i])
        else:
            counter = 1
            while len(stack) != 0 and stack[-1] <= temperatures[i]:
                result[i-counter] = counter
                counter += 1
                stack.pop()
    return result
#wrong answer

# def dailyTemperatures(self, temperatures):
#     answer = [0] * len(temperatures)
#     stack = []
#     for i, cur in enumerate(temperatures):
#         while stack and cur > temperatures[stack[-1]]:
#             last = stack.pop()
#             answer[last] = i - last
#         stack.append(i)

#     return answer
