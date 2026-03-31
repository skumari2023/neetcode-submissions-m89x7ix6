class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #return the list of the hashmap values
        #key = freq of chars & val = the list of strings

        result = defaultdict(list)

        for s in strs:
            freq = [0] * 26 
            for c in s:
                freq[ord(c) - ord('a')] += 1
            
            key = tuple(freq)
            result[key].append(s)
        
        return list(result.values())