class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        check=[]
        for i in range(0,m):
            check.append([False]*n)
        
        def dfs(i,j,k):
            if k==len(word):
                return True
            if not(0<=i<m and 0<=j<n):
                return False
            if board[i][j]!=word[k] or check[i][j]==True:
                return False
            check[i][j]=True
            for dx, dy in directions:
                if dfs(i + dx, j + dy, k+1):
                    return True

            check[i][j] = False
            return False
        
        for i in range(0,m):
            for j in range(0,n):
                if board[i][j]==word[0] and dfs(i,j,0):
                    return True
        return False
                    
                    