class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        number = set (nums)
        
        if len(number) != len(nums):
            return True
        
        return False