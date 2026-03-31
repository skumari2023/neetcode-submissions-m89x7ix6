class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #key: freq --> val = int 
        #return the top k most freq
        #for loop returning values until k is reached

        count = {}
        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        #+1 bc length could go from 0 --> len of nums
        freq = [[] for i in range(len(nums) + 1)]
        
        for num, c in count.items():
            freq[c].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res



