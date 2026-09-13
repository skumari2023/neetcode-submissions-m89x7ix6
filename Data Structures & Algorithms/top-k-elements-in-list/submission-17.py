class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        h1 = {}
        freq = [[] for i in range(len(nums) + 1)]
        output = []
        length = len(nums)

        for n in nums:
            h1[n] = h1.get(n,0) + 1
        
        for n in h1.keys():
            freq[h1[n]].append(n)

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                output.append(n)
                if len(output) == k:
                    return output
        


            
        
