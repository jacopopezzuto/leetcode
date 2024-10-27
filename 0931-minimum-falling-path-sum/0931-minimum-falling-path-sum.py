class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix),len(matrix[0])
        for i in range(1,m):
            for j in range(0,n):
                tl=float("+inf") if j-1<0 else matrix[i-1][j-1]
                tt=matrix[i-1][j]
                tr=float("+inf") if j+1>m-1 else matrix[i-1][j+1]
                matrix[i][j]+=min(tl,tt,tr)
        result=float("+inf")
        for i in range(0,n):
            result=min(result,matrix[m-1][i])
        return result