class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        count=0
        def bfs(i,j):
            for x,y in directions:
                nx,ny = i+x, j+y
                if 0<=nx<m and 0<=ny<n and grid[nx][ny]=="1":
                    grid[nx][ny]="2"
                    bfs(nx,ny)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    bfs(i,j)
                    count+=1
        return count