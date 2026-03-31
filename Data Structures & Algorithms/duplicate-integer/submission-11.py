class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: #use hashsets bc do not require indices
        m = set();
        for n in nums:
            if n in m:
                return True #in python the True and False are capitalized
            m.add(n) #use add in sets 
        return False
