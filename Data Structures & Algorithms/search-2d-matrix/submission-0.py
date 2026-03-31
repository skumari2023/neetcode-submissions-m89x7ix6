class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows * cols - 1        
        
        while (low <= high):
        # to map a 1D array to 2D divide by cols = row index & % by cols = col index
            mid = (low + high) // 2
            row = mid // cols
            col = mid % cols

            value = matrix[row][col]

            if (value < target):
                low = mid + 1
            
            elif (value > target):
                high = mid - 1
           
            else:
                return True
        
        return False