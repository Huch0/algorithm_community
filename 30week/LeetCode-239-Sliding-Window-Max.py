from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # cur_max = -10000
        # #last = 0
        # window = deque()
        # result = []
        # # for i in range(0, k):
        # #     if max < nums[i]:
        # #         max = nums[i]
        # #         last = i
        # #     window.append(nums[i])
        
        # # result = [max]

        # for i, v in enumerate(nums):
        #     window.append(v)

        #     if i < k-1:
        #         continue

        #     if cur_max == -10000:
        #         cur_max = max(window)
        #     elif v > cur_max:
        #         cur_max = v

        #     result.append(cur_max)

        #     if cur_max == window.popleft():
        #         cur_max = -10000

        # return result
        
        ################
        result = []
        # 윈도우의 최대값의 인덱스를 유지할 덱
        deq = deque()

        for i in range(len(nums)):
            # 덱의 맨 앞이 현재 윈도우 범위를 벗어났는지 확인
            if deq and deq[0] < i - k + 1:
                deq.popleft()
            
            # 현재 숫자가 덱의 맨 뒤에 있는 숫자보다 크거나 같으면,
            # 덱의 맨 뒤에 있는 숫자가 현재 숫자보다 크거나 같을 때까지
            # 덱에서 제거합니다.
            while deq and nums[i] >= nums[deq[-1]]:
                deq.pop()

            # 현재 숫자의 인덱스를 덱에 추가합니다.
            deq.append(i)

            # 윈도우의 크기가 k가 되면, 덱의 맨 앞에 있는 인덱스의
            # 숫자를 결과 리스트에 추가합니다.
            if i >= k - 1:
                result.append(nums[deq[0]])

        return result