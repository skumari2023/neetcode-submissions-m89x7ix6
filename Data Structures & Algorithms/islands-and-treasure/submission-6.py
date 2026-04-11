class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
        
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        dist = 0
        
        while q:
            for i in range(len(q)):
                
                r,c = q.popleft()
                grid[r][c] = dist 

                for dr,dc in directions:
                    row = dr + r
                    col = dc + c

                    if row < 0 or col < 0 or row > rows - 1 or col > cols - 1 or grid[row][col] == -1 or (row,col) in visited:
                        continue 

                    q.append([row,col])
                    visited.add((row,col))
            dist += 1


                    