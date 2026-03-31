class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        duplicate = set()
        for num in nums:
            duplicate.add(num)
        
        if len(nums) != len(duplicate):
            return True
        
        return False 
