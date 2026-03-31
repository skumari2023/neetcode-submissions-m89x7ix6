class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0 
        maxlength = 0 
        set1 = set()

        for right in range(0, len(s), 1):
            
            while s[right] in set1:
                set1.remove(s[left])
                left += 1
                
            set1.add(s[right])
            
            maxlength = max(maxlength, right - left + 1) #it's length add 1
        
        return maxlength