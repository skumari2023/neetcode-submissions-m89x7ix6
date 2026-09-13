class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        h1 = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            h1[tuple(freq)].append(s)
        
        return list(h1.values())
