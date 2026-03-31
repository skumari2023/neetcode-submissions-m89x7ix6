class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        l = 0
        output = []

        for i,n in enumerate(nums):
            
            if i > 0 and n == nums[i-1]:
                continue
           
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                if (nums[l] + nums[r]) < -n:
                    l+=1
                elif (nums[l] + nums[r]) > -n:
                    r-=1
                else:
                    output.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1

        return output
                



                

        