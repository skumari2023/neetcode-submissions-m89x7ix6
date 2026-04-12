class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num = set(nums)
        maxLength = 0
        #iterate over the set instead of nums bc duplicates could cause wasted time
        for n in num:
            if (n - 1) not in num:
                length = 1
                while (n + length) in num:
                    length += 1
                maxLength = max(maxLength, length)
        return maxLength 