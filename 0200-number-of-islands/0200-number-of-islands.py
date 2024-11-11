class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        count=0
        check=[]
        for i in range(m):
            check.append([False]*n)
        def dfs(i,j):
            if not (0<=i<m and 0<=j<n) or check[i][j]==True or grid[i][j]!="1":
                return 
            check[i][j]=True
            for dx,dy in directions:
                dfs(i+dx,j+dy)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and check[i][j]==False:
                    count+=1
                    dfs(i,j)
        return count