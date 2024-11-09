class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m,n = len(moveTime),len(moveTime[0])
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        visited=[]
        for i in range(m):
            visited.append([False]*n)
        # time,i,j,move_cost
        min_heap=[[0,0,0,2]]
        while min_heap:
            time,i,j,move_cost=heappop(min_heap)
            if i==m-1 and j==n-1:
                return time
            for dx,dy in directions:
                nx,ny = i+dx,j+dy
                if 0<=nx<m and 0<=ny<n:
                    if visited[nx][ny]==True:
                        continue
                    visited[nx][ny]=True
                    new_move_cost=2 if move_cost==1 else 1
                    new_time=max(time+new_move_cost,moveTime[nx][ny]+new_move_cost)
                    heapq.heappush(min_heap,(new_time,nx,ny,new_move_cost))
        return -1