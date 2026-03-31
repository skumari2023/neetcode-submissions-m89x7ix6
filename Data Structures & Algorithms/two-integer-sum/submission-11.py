class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        number = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in number: #checks keys not values
                return [number.get(diff), i]
            else:
                number[n] = i
        