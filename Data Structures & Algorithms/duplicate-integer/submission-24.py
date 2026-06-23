class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        num = set()

        for n in nums:
            num.add(n)
        
        if len(num) != len(nums):
            return True
        else:
            return False