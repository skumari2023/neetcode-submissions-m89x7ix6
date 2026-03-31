class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        hashMap = defaultdict(list)

        for s in strs:
            
            frequency = [0] * 26

            for c in s:
                #accesses ascii value or the index (1-26)
                frequency[ord(c) - ord("a")] += 1
            
            #remember cannot use mutable/changeable items (lists) as keys --> tuple
            if tuple(frequency) in hashMap:
                hashMap[tuple(frequency)].append(s)
            
            else:
                hashMap[tuple(frequency)] = [s] #make sure you are returning a list        
        
        return list(hashMap.values()) #makes sure a list is returned
        


        