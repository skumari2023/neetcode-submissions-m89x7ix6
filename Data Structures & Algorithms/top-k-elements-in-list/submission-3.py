class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #count the freq of the numbers
        #bucket sort 
        #append to result until it reaches len of k

        count = {}
        output = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # 0 --> len(nums)
        freq = [[] for i in range(len(nums) + 1)]
        
        for num, c in count.items():
            freq[c].append(num)
        
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                output.append(num)
                if len(output) == k:
                    return output

