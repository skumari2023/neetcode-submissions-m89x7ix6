class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #you know it is sliding window when you are working with arrays/strings
        #and look for optimal subranges (ex: max/min sum) with a condition
        # + brute force = slow 

        #maxP = 0 
        #for n in range(len(prices)):
        #    for i in range (n+1, len(prices), 1):
        #        if (prices[i] - prices[n]) > maxP:
        #            maxP = prices[i] - prices[n]
        #return maxP
                
        left = 0
        right = 1
        maxP = 0

        while right < len(prices):

            if (prices[left] < prices[right]):
                maxP = max((prices[right] - prices[left]), maxP)
        
            else:
                left = right 
            
            right += 1

        return maxP
        
        

        
        