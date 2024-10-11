class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(0,len(matrix)):
            j=0
            while j!=i:
                dummy=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=dummy
                j+=1
        j=len(matrix)-1
        k=0
        while k<j:
            for i in range(0,len(matrix)):
                dummy = matrix[i][k]
                matrix[i][k] = matrix[i][j]
                matrix[i][j] = dummy
            j-=1
            k+=1