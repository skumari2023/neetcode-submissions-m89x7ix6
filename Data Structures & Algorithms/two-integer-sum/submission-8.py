class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #input = array on integers (nums), integer (target)
        #nums[i] + nums[j] == target 
        #return the smallest index, bigger index

        hashMap = {}

        for index, num in enumerate (nums):

            difference = target - num

            if difference in hashMap:
                return [hashMap[difference] , index]
            
            else:
                hashMap[num] = index


