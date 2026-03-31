class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set() 
        #should be outside the loop, keeps creating new sets (will only have 1 element each time)
        for i in range (0, len(nums), 1):
            mySet.add(nums[i])
        
        if len(mySet) != len(nums):
                return True
        else:
            return False
        
        