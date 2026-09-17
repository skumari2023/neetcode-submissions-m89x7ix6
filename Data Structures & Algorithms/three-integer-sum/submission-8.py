class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        start = 0
        res = []

        while start < len(nums) - 2:
            if start > 0 and nums[start] == nums[start - 1]:
                start += 1
                continue 
            l = start + 1
            r = len(nums) - 1
            while l < r and start < l and start < r:
                if (nums[start] + nums[l] + nums[r]) < 0:
                    l += 1
                elif (nums[start] + nums[l] + nums[r]) > 0:
                    r -= 1
                else:
                    res.append([nums[start], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
            start += 1
        return res
            