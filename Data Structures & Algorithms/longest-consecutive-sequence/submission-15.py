class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num = set(nums)
        maxLen = 0 

        for n in nums:
            length = 0
            if (n-1) not in num:
                length = 1
                while (n+1) in num:
                    length += 1
                    n += 1 #forgot to update this
            if maxLen < length:
                maxLen = length 
        
        return maxLen
