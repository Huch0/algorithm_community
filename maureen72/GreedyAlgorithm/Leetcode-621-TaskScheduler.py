class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        cnt = collections.Counter(tasks)
        result = 0

        while True:
            subCnt = 0
            # 갯수대로 추출
            for task,i in cnt.most_common(n+1):
                subCnt +=1
                result+=1

                cnt.subtract(task)
                cnt += collections.Counter()

            if not cnt:
                break

            result = result + n - subCnt + 1
        return result