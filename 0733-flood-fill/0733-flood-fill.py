class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m,n=len(image),len(image[0])
        queue=deque()
        starting_color=image[sr][sc]
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        if starting_color==color:
            return image
        queue.append((sr,sc))
        while queue:
            x,y=queue.popleft()
            image[x][y]=color
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and image[nx][ny]==starting_color:
                    queue.append([nx,ny])
        return image