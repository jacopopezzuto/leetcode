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
        m,n=len(grid),len(grid[0])
        count=0
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        queue=deque()
        def bfs():
            while queue:
                i,j=queue.popleft()
                for dx,dy in directions:
                    nx,ny=i+dx,j+dy
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny]=="1":
                        grid[nx][ny]="2"
                        queue.append([nx,ny])
                    
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    count+=1
                    queue.append([i,j])
                    bfs()
        return count