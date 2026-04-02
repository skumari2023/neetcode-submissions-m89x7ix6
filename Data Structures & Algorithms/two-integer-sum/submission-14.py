class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mp = {}

        for i,n in enumerate(nums):
            val = target - n
            if val in mp:
                return [mp[val], i]
            else:
                mp[n] = i 