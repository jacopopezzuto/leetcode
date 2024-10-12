class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n=len(matrix),len(matrix[0])
        result=[]
        for i in range(0,n):
            result.append([0]*m)
        for i in range(0,m):
            for j in range(0,n):
                result[j][i]=matrix[i][j]
        return result