class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board), len(board[0])
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        def dfs(i,j,k,visited):
            if k==len(word):
                return True
            if not(0<=i<m and 0<=j<n):
                return False
            if board[i][j]!=word[k] or visited[i][j]==True:
                return False
            visited[i][j]=True
            for di, dj in directions:
                if dfs(i + di, j + dj, k + 1, visited):
                    return True

            visited[i][j] = False
            return False
        visited=[]
        for i in range(0,m):
            visited.append([False]*n)
        
        for i in range(0,m):
            for j in range(0,n):
                if dfs(i,j,0,visited)==True:
                    return True
        return False