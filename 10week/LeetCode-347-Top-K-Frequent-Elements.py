import collections
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freqs = collections.Counter(nums)
        freqs_table = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
        topk = freqs_table[:k]
        return [item[0] for item in topk]

        # freqs_heap = []
        # for f in freqs:
        #     # 힙에 음수로 삽입 
        #     # -> 최소 힙 구성 
        #     # -> 가장 작은 음수 순으로 추출
        #     # -> 가장 높은 빈도 순으로 추출
        #     heapq.heappush(freqs_heap, (-freqs[f], f))

        # topk = list()
        # # k번 만큼 추출, 최소 힙(Min Heap)이므로 가장 작은 음수 순으로 추출
        # for _ in range(k):
        #     topk.append(fr)
        
        # return topk