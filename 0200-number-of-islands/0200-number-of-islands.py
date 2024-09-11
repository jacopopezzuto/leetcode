class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter=0
        def markIsland(i,j,n,m):
            if i>=n or j>=m or i<0 or j<0 or grid[i][j] == '0' or grid[i][j]=='2':
                return
            else:
                grid[i][j] = '2'
                markIsland(i+1,j,n,m)
                markIsland(i,j+1,n,m)
                markIsland(i-1,j,n,m)
                markIsland(i,j-1,n,m)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    markIsland(i,j,len(grid),len(grid[0]))
                    counter+=1
        return counter
    