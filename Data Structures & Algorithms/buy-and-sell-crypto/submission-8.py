class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        maxP = 0

        for r in range(len(prices)):

            while prices[r] < prices[l]:
                l = r
            
            maxP = max(maxP, prices[r] - prices[l])
        
        return maxP


        