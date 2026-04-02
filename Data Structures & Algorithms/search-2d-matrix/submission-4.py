class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        i = 0
        while i < len(matrix):
            l = 0
            r = len(matrix[i]) - 1
            while l <= r:
                mid = (l+r) // 2
                if matrix[i][mid] < target:
                    l = mid + 1
                elif matrix[i][mid] > target:
                    r = mid - 1
                elif matrix[i][mid] == target:
                    return True
            i+=1
        return False


