class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num = set(nums)
        maxLength = 0
        length = 0

        for n in nums:
            if (n-1) not in num:
                length = 1
                while (n+1) in num:
                    length += 1
                    n += 1
            if length > maxLength:
                maxLength = length
        
        return maxLength
            
            
        