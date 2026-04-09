class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #skip duplicates

        nums.sort()
        output = []

        for i in range(len(nums)):
            
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeS = nums[i] + nums[l] + nums[r]
                if threeS < 0:
                    l += 1
                elif threeS > 0:
                    r -= 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        return output 

