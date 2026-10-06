class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        bucket = [[] for i in range(len(nums) + 1)]

        h1 = {}

        for n in nums:
            h1[n] = h1.get(n,0) + 1
        
        for key, v in h1.items():
            bucket[v].append(key)
        
        for i in range(len(nums), -1, -1):
            for c in bucket[i]:
                res.append(c)
                if len(res) == k:
                    return res
