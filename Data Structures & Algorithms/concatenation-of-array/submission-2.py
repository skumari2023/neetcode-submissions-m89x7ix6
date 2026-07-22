class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        num = [] 
        for i in range(len(nums)):
            num.insert(i, nums[i])
            num.insert(i+len(nums), nums[i])
        return num
