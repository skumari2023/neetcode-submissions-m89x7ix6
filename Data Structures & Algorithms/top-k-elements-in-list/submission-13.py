class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        heap = []

        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
        
        while len(heap) > k:
            heapq.heappop(heap)

        output = []
        while len(output) < k:
            output.append(heapq.heappop(heap)[1])
        return output