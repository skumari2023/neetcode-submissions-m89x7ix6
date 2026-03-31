class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #just using the diff to check if it is in the hashmap
        #populate the value n and its index in the hashmap

        sum = {}

        for i, n in enumerate(nums):
            
            diff = target - n

            if diff in sum:
                return [sum[diff], i]
            
            else:
                sum[n] = i