class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #val = list of strings, key = freq
        #freq = array (sorted alr)
        #return values of hashmap as a list 

        result = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            key = tuple(freq)
            result[key].append(s)
        
        return list(result.values())
