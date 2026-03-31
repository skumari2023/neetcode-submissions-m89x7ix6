class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #freq = key --> val = list

        result = defaultdict(list)

        for s in strs:
            freq = [0] * 26 #resets for every string

            for c in s:
                freq[ord(c) - ord('a')] += 1
           
            key = tuple(freq) #cannot use lists as keys in hashmaps
            result[key].append(s)
        
        return list(result.values())
        