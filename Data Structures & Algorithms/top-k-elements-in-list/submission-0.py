class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #key --> values
        #diff keys --> same value

        hashmap = {}
        output = []

        for num in nums:
            
            if num in hashmap:
                hashmap[num] += 1
            
            else:
                hashmap[num] = 1
        
        maxFreq = len(nums)


        for i in range (len(nums), 0, -1):
            
            for key, value in hashmap.items(): #did not know the syntax for this
                
                if value == i:
                    output.append(key)

                if len(output) == k:
                    return output


        