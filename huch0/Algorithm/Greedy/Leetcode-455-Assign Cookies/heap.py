class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Put elements into the heap for greedy
        hg = []
        hs = []
        for gr in g:
            heapq.heappush(hg, gr)
        for si in s:
            heapq.heappush(hs, si)

        cnt = 0  # Count of children who can be satisfied
        while hg:
            cur_g = heapq.heappop(hg)

            while hs:
                cur_s = heapq.heappop(hs)

                if cur_g <= cur_s:
                    cnt += 1
                    break
            # There is no remaining cookies
            if not hs:
                break

        return cnt
