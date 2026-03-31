class Solution:
    def trap(self, height: List[int]) -> int:
        
        #edgecase - if height is empty 

        if not height:
            return 0

        output = 0 
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]

        while (left < right):

            if (maxLeft < maxRight):
                left += 1
                maxLeft = max(maxLeft, height[left])
                output += maxLeft - height[left]

            
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                output += maxRight - height[right]
        
        return output 