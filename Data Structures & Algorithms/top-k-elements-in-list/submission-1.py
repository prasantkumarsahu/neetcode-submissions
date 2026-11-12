import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        pq = []

        for num, count in frequency.items():
            heapq.heappush(pq, (count, num))

            if len(pq) > k:
                heapq.heappop(pq)

        return [num for count, num in pq]
