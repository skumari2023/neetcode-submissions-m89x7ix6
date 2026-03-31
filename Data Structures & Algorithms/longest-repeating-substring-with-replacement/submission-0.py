class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #input = uppercase characters + integer (k) 
        #replace k number of characters with diff uppercase characters
        #output = length of longest substring with only 1 unique character

        set1 = set(s)
        maxlength = 0

        for c in set1:

            count = left = 0

            for right in range(len(s)):

                if s[right] == c:
                    count += 1
                
                while (right - left + 1) - count > k:
                    
                    if s[left] == c:
                        count -= 1
                    
                    left += 1
                
                maxlength = max(maxlength, right - left + 1)
        
        return maxlength 



        