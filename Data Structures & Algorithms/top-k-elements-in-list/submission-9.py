class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count1 = Counter(nums)
        output = []

        freq = [[]for i in range(len(nums)+1)]

        for num, count in count1.items():
            freq[count].append(num)
        
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                output.append(num)
                if len(output) == k:
                    return output
