class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Input: grid = [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ]
        Output: 1
        
        '''
        if not grid:
            return 0
        m,n=len(grid),len(grid[0])
        count=0
        def dfs(r, c):
            if (
                r < 0
                or c < 0
                or r >= len(grid)
                or c >= len(grid[0])
                or grid[r][c] != "1"
            ):
                return 
            
            grid[r][c] = "2"

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count
            