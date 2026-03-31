class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: #lists can have duplicates, sets cannot
        m = [];
        for n in nums:
            if n in m:
                return True #in python the True and False are capitalized
            m.append(n) #use append in lists 
        return False
