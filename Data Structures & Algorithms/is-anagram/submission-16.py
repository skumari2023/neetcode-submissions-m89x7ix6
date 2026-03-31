class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #key will be the character 
        #frequency = value
        
        hashS = {}
        hashT = {}

        for val in s:
            if val in hashS:
                hashS[val] += 1
           
            else:
                hashS[val]  = 1

        for value in t:
            if value in hashT:
                hashT[value]  += 1
            else:
                hashT[value]  = 1
        
        if hashS != hashT:
            return False
        
        return True
