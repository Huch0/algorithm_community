class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the number of each elements
        frequencies = collections.Counter(nums)

        frequency_heap = []
        for element in frequencies.keys():
            # Push to min heap (-frequency, element)
            heapq.heappush(frequency_heap, (-frequencies[element], element))

        k_most_frequents = []
        for i in range(k):
            # Extract most frequent element from heap k times.
            k_most_frequents.append(heapq.heappop(frequency_heap)[1])

        return k_most_frequents