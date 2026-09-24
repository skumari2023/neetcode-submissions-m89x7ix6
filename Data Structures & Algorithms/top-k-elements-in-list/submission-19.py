class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        bucket = [[] for i in range(len(nums) + 1)]
        hash1 = {}
        res = []

        for n in nums:
            hash1[n] = hash1.get(n, 0) + 1 #if you don't get anything return 0
        
        for key,val in hash1.items(): #don't name key to be k bc it confuses with the input k
            bucket[val].append(key)
        
        for i in range(len(nums), -1, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res