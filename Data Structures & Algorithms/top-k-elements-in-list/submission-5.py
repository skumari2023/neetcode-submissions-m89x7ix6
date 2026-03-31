class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        output = []

        freq = [[] for i in range(len(nums) + 1)]

        for num, c in count.items():
            freq[c].append(num)
        
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                output.append(num)
                if len(output) == k:
                    return output

