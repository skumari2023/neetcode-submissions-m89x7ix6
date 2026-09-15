class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        h1 = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for n in nums:
            h1[n] = h1.get(n,0) + 1
        
        for key,val in h1.items(): 
    #don't name this variable k it's overwritten by the global variable
            freq[val].append(key)
        
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
