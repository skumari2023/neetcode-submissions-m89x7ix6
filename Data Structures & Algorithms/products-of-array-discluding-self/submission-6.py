class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [0] * len(nums)
        prefix = 1
        post = 1

        for i in range(len(nums)): 
            output[i] = prefix 
            prefix *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            output[i] *= post 
            post *= nums[i] 
        
        return output