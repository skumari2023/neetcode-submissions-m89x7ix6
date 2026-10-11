class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0 
        ans = 0

        for r in range(len(prices)):

            while prices[r] < prices[l] and l < r:
                l += 1
            
            ans = max(ans, prices[r] - prices[l])

        return ans