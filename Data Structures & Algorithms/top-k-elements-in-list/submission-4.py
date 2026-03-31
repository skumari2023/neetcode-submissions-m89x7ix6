class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        res = []

        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        freq = [[] for i in range(len(nums) + 1)]

        for c,num in count.items():
            freq[num].append(c)
        
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

