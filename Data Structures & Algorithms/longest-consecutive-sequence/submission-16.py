class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num = set(nums)
        maxLength = 0

        for n in num:
            length = 0
            if (n-1) not in num:
                length = 1
                while (n+1) in num:
                    length += 1
                    n += 1
            maxLength = max(length, maxLength)
        
        return maxLength
