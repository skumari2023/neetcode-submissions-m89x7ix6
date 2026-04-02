class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        mp = {}

        for n in nums:
            if n in mp:
                return True
            mp[n] = n
        return False