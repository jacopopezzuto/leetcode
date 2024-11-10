class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m,n=len(moveTime),len(moveTime[0])
        check=[]
        for i in range(m):
            check.append([False]*n)
        check[0][0]=True
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        #time,i,j
        queue=[[0,0,0]]
        heapq.heapify(queue)
        while queue:
            time,i,j=heapq.heappop(queue)
            if i==m-1 and j==n-1:
                return time
            for dx,dy in directions:
                nx,ny=i+dx,j+dy
                if 0<=nx<m and 0<=ny<n and check[nx][ny]==False:
                    new_time=max(time+1,moveTime[nx][ny]+1)
                    check[nx][ny]=True
                    heapq.heappush(queue,[new_time,nx,ny])
        return -1
            