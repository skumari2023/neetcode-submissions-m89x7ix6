class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        output = []

        for i,n in enumerate(nums):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeS = n + nums[l] + nums[r]

                if threeS > 0:
                    r-=1
                elif threeS < 0:
                    l+=1
                else:
                    output.append([n, nums[l], nums[r]])
                    l+=1
                    r-=1

                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
        return output 

        