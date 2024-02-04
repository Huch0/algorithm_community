# mydict.keys() / mydict.values() / mydict.items()로 각각 키/값/키-값 쌍을 가져올 수 있음
class Solution: # dict에 키-값으로 수-빈도를 모두 저장한 후 정렬하기
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        mydict = collections.defaultdict(int)
        for n in nums:
            mydict[n] = mydict[n] + 1
        mylist = [(-item, key) for (key, item) in mydict.items()]
        mylist.sort()
        for i in range(k):
            answer.append(mylist[i][1])
        return answer

class Solution: # Counter 사용해보기
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        answer = []
        for n, freq in collections.Counter(nums).items():
            heapq.heappush(pq, (-freq, n))
        for i in range(k):
            answer.append(heapq.heappop(pq)[1])
        return answer