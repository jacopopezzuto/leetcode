class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter=0
        m,n=len(grid),len(grid[0])
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        def countIslands(i,j):
            if not(0<=i<m and 0<=j<n) or grid[i][j]!="1":
                return 
            grid[i][j]=2
            for x,y in directions:
                countIslands(i+x,j+y)
        
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j]=="1":
                    countIslands(i,j)
                    counter+=1
        return counter
    