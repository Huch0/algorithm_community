class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # for store days that weren't decided yet
        stack = []
        # initialize list with size
        # because elements will not be appended sequentially
        answers = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack:
                # pop last element from stack
                stack_i = stack.pop()

                # (stack_i)th day find warmer day
                if temperatures[stack_i] < t:
                    answers[stack_i] = i - stack_i
                else:
                    # (stack_i)th day doesn't find warmer day so push again to stack.
                    stack.append(stack_i)
                    break
            
            stack.append(i)
        
        return answers
        