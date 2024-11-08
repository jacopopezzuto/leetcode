# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m,n=binaryMatrix.dimensions()
        i,j=0,n-1
        result=-1
        while 0<=i<m and 0<=j<n:
            if binaryMatrix.get(i,j)==0:
                i+=1
            else:
                result=j
                j-=1
        return result