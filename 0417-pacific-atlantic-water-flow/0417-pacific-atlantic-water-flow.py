class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights),len(heights[0])
        pacific,atlantic=[],[]
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        for i in range(0,m):
            pacific.append([False]*n)
            atlantic.append([False]*n)
        def bfs(queue,ocean):
            while queue:
                x,y=queue.popleft()
                for dx,dy in directions:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<m and 0<=ny<n and heights[nx][ny]>=heights[x][y] and ocean[nx][ny]!=True:
                        queue.append([nx,ny])
                        ocean[nx][ny]=True
        
        pacific_q=deque()
        for i in range(0,n):
            pacific[0][i]=True
            pacific_q.append([0,i])
        for i in range(0,m):
            pacific[i][0]=True
            pacific_q.append([i,0])
        bfs(pacific_q,pacific)
        atlantic_q=deque()
        for i in range(0,m):
            atlantic[i][n-1]=True
            atlantic_q.append([i,n-1])
            
        for i in range(0,n):
            atlantic[m-1][i]=True
            atlantic_q.append([m-1,i])
        bfs(atlantic_q,atlantic)
        result=[]
        for i in range(0,m):
            for j in range(0,n):
                if pacific[i][j]==True and atlantic[i][j]==True:
                    result.append([i,j])
        return result