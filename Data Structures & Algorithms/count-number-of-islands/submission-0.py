class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        total = 0

        def dfs(r,c):
            if r < 0 or r > rows - 1 or c < 0 or c > cols - 1 or grid[r][c] == "0":
                return

            #DOES NOT ADD REPEATS
            grid[r][c] = "0"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i,j)
                    total += 1
        
        return total
