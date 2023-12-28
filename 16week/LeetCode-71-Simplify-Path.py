import re

class Solution:
    def simplifyPath(self, path: str) -> str:
        # '/'가 1개 이상 모여있는 패턴으로 분리
        dirs = re.split('/+', path)
        
        dirs_copy = dirs[:]
        # '.' 제거
        for i in range(len(dirs)):
            if dirs[i] == "." or dirs[i] == '':
                dirs_copy.remove(dirs[i])

        # '..' 처리
        # 생각해야하는 것은 /.. 은 그냥 /이라는 것!
        # 고로 정상적인 dir을 스택에 넣고 ..을 만나면 pop하면 됨.

        stack = []

        for i in range(len(dirs_copy)):
            if dirs_copy[i] == "..":
                if stack:
                    stack.pop()
                else:
                    pass
            else:
                stack.append(dirs_copy[i])

        if not stack:
            return '/'
        
        stack.append('')
        result = '/'.join(stack)

        return '/' + result[:-1]
