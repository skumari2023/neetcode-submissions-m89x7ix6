class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        set1 = set(nums)
        maxL = 0
        length = 0

        for n in nums:
            
            if n-1 not in set1:
                length = 1
                while n + length in set1:
                    length += 1
            maxL = max(maxL, length)
        
        return maxL