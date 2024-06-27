class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answers = []
        stack = [('(', 1, 0)]
        while stack:
            path, o, c = stack.pop()
            # print(stack, path, o, c)

            if c == n:
                # if self.is_answer(path):
                answers.append(path)
                continue

            if o + 1 <= n:
                stack.append((path + '(', o + 1, c))
            if c + 1 <= o:
                stack.append((path + ')', o, c + 1))

        return answers
