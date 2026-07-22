class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        num = [0] * (2 * len(nums)) 
        for i in range(len(nums)):
            num[i] = nums[i]
            num[i + len(nums)] = nums[i]
        return num
