class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        check = ""

        for c in s:
            if c.isalnum() == True:
                check += c.lower()
        
        l = 0
        r = len(check) - 1

        while l < r: 
            if check[l] == check[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
        

