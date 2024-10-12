class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        maxLocal = []
        for i in range(0,n-2):
            maxLocal.append([0]*(n-2))
        for i in range(0,n-2):
            for j in range(0,n-2):
                maxLocal[i][j]=self.findMax(grid,i,j)
        return maxLocal
    
    def findMax(self,grid,x,y):
        n_max=0
        n=len(grid)
        for i in range(x,x+3):
            for j in range(y,y+3):
                n_max=max(n_max,grid[i][j])
        return n_max
                