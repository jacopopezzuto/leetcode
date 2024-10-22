class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights), len(heights[0])
        pacific,atlantic=[],[]
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        for i in range(0,m):
            pacific.append([False]*n)
            atlantic.append([False]*n)
        
        def bfs(queue,array):
            while queue:
                x,y=queue.popleft()
                for dx,dy in directions:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<m and 0<=ny<n and not array[nx][ny] and heights[nx][ny]>=heights[x][y]:
                        queue.append([nx,ny])
                        array[nx][ny]=True
            
        pacific_queue=deque()
        for i in range(0,n):
            pacific_queue.append([0,i])
            pacific[0][i]=True
            bfs(pacific_queue,pacific)
        for i in range(0,m):
            pacific_queue.append([i,0])
            pacific[i][0]=True
            bfs(pacific_queue,pacific)
        
        atlantic_queue=deque()
        for i in range(0,m):
            atlantic_queue.append([i,n-1])
            atlantic[i][n-1]=True
            bfs(atlantic_queue,atlantic)
        for i in range(0,n):
            atlantic_queue.append([m-1,i])
            atlantic[m-1][i]=True
            bfs(atlantic_queue,atlantic)
        result=[]
        for i in range(0,m):
            for j in range(0,n):
                if atlantic[i][j]==pacific[i][j]==True:
                    result.append([i,j])
        return result
            
        
        atlantic_queue=deque()