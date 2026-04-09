class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        heap = []

        for i in count.keys():
            heapq.heappush(heap, (count[i], i))
            while len(heap) > k:
                heapq.heappop(heap)
        
        output = []
        while heap:
            output.append(heapq.heappop(heap)[1])
        return output
        

