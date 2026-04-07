class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count1 = Counter(nums)
        output = []

        heap = []
        for num in count1.keys():
            heapq.heappush(heap, (count1[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        for i in range(k):
            output.append(heapq.heappop(heap)[1])
        return output 