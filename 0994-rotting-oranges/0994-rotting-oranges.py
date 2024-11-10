class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = collections.deque()
        fresh = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))     # initial rotten oranges (at t = 0)
                elif grid[r][c] == 1:
                    fresh += 1               # initial fresh oranges
        
        neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        time = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in neighbors:
                    nr, nc = row + dr, col + dc
                    if nr not in range(rows) or nc not in range(cols) or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
            time += 1
        return time if fresh == 0 else -1