class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix=[]
        for i in range(0,m):
            matrix.append([0]*n)
        matrix[0][0]=1
        for i in range(1,n):
           matrix[0][i]+=matrix[0][i-1]    
        for i in range(1,m):
           matrix[i][0]+=matrix[i-1][0]  
        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j]+=matrix[i-1][j]+matrix[i][j-1]
        return matrix[-1][-1]