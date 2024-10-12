class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n=len(mat),len(mat[0])
        if r*c != m*n:
            return mat
        result= []
        for i in range(0,r):
            result.append([0]*c)
        k,z=0,0
        for i in range(0,m):
            for j in range(0,n):
                result[z][k]=mat[i][j]
                k+=1
                if k==c:
                    z+=1
                    k=0
        return result