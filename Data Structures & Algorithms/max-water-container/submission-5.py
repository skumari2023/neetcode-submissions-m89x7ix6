class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxArea = 0 
        l = 0 
        r = len(heights) - 1

        while l < r:
            maxArea = max(maxArea, (min(heights[l], heights[r]) * (r - l)))
            if heights[l] < heights[r]:
                l += 1
            else: #do not use another if statement here because it will check it right after it updates the if statement before
                r -= 1
        
        return maxArea