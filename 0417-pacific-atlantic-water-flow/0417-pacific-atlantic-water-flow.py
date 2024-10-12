class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M,N = len(heights), len(heights[0])
        pacific_reachable, atlantic_reachable = [], []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for i in range(0,M):
            pacific_reachable.append([False]*N)
            atlantic_reachable.append([False]*N)
        
        def bfs(queue: deque, reachable: List[List[bool]]):
            while queue:
                x,y=queue.popleft()
                reachable[x][y]=True
                for i,j in directions:
                    nx,ny = x+i,y+j
                    if 0 <= nx < M and 0 <= ny < N and not reachable[nx][ny]:
                        if heights[nx][ny] >= heights[x][y]:
                            queue.append((nx, ny))
        
        pacific_queue=deque()
        for i in range(0,N):
            pacific_queue.append((0,i))
            pacific_reachable[0][i]=True
        for i in range(0,M):
            pacific_queue.append((i,0))
            pacific_reachable[i][0]=True
        bfs(pacific_queue, pacific_reachable)
        
        atlantic_queue=deque()
        for i in range(0,N):
            atlantic_queue.append((M-1,i))
            atlantic_reachable[M-1][i]=True
        for i in range(0,M):
            atlantic_queue.append((i,N-1))
            atlantic_reachable[i][N-1]=True
        bfs(atlantic_queue, atlantic_reachable)
        
        result=[]
        for i in range(0,M):
            for j in range(0,N):
                if atlantic_reachable[i][j]==True and pacific_reachable[i][j]==True:
                    result.append([i,j])
        return result