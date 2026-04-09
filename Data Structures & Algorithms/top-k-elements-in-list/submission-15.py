class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)

        freq = [[] for f in range(len(nums) + 1)]

        for num, c in count.items():
            freq[c].append(num)
        
        output = []

        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                output.append(num)
                if len(output) == k:
                    return output