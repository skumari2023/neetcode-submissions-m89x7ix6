class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        ans = []

        for i,n in enumerate(nums):
            if (target - n) in hashmap:
                ans.append(hashmap[target-n])
                ans.append(i)
            else:
                hashmap[n] = i
        
        return ans
