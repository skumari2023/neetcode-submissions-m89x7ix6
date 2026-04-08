class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            while len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res

