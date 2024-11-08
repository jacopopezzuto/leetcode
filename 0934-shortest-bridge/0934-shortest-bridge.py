class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        starting_coordinates=[0,0]
        found = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    starting_coordinates = [i, j]
                    found = True
                    break
            if found:
                break
        first_island=deque([starting_coordinates])
        grid[starting_coordinates[0]][starting_coordinates[1]]=2
        ocean=deque([starting_coordinates])
        while first_island:
            i,j=first_island.popleft()
            for x,y in directions:
                nx,ny=i+x,j+y
                if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1:
                    grid[nx][ny]=2
                    first_island.append([nx,ny])
                    ocean.append([nx,ny])
        count = 0
        while ocean:
            for _ in range(len(ocean)):
                i, j = ocean.popleft()
                for x, y in directions:
                    nx, ny = i + x, j + y
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 1:
                            return count
                        elif grid[nx][ny] == 0:
                            grid[nx][ny] = 3
                            ocean.append([nx, ny])
            count += 1
        return -1