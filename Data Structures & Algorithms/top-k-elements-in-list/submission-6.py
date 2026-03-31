class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mp = Counter(nums)
        output = []

        freq = [[] for i in range(len(nums)+1)]

        for n,count in mp.items():
            freq[count].append(n)
        
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                output.append(n)
                if len(output) == k:
                    return output

        