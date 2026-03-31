class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #REMEMBER THIS SYNTAX
        hashSet = set()

        for i in nums:
            hashSet.add(i)
        
        if len(hashSet) < len(nums):
            return True
        
        return False
