class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #key = char freq, value = string 
        #the value has to be a list 
        #want to output the contents of the hashmap 
        #have to check char frequency for each string

        #cannot use a list as a key bc they must be immutable/hashable 
        #use tuple

        charF = defaultdict(list)

        for s in strs:

            arr = [0] * 26
            
            for c in s:
                arr[ord(c) - 97] += 1
            
            if tuple(arr) in charF:
                charF[tuple(arr)].append(s)
            else:
                charF[tuple(arr)] = [s]
        
        return list(charF.values())
            
