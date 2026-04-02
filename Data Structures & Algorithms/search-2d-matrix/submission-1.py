class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        res = []
        for m in matrix:
            res.extend(m)

        l = 0
        r = len(res) - 1

        while l <= r:
            mid = (l+r) // 2
            if res[mid] < target:
                l = mid + 1
            elif res[mid] > target:
                r = mid - 1
            else:
                return True
        return False
