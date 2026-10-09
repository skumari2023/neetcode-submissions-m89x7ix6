class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0 
        curr = 0 
        ans = 0

        for r in range(1, len(prices), 1):
            curr = prices[r] - prices[l]

            while prices[r] < prices[l]:
                l = r
            
            ans = max(ans, curr)

        return ans
                