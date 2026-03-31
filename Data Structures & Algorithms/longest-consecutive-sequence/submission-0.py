class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #hashset = O(1) lookups
        
        long = set(nums)
        maxSeq = 0
        length = 0

        for n in long:
            if n-1 not in long:
                length = 1
                while n+length in long:
                    length += 1
                maxSeq = max(maxSeq, length)
        
        return maxSeq
                
            

