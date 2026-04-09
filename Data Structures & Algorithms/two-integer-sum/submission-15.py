class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        tSum = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in tSum:
                return [tSum[diff], i]
            tSum[n] = i