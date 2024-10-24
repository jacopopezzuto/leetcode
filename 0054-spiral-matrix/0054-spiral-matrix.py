class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])
        level=0
        result=[]
        while level<(min(m, n) + 1) // 2:
            
            #from left to right
            for i in range(level, n - level):
                result.append(matrix[level][i])
            
            #from top to bottom
            for i in range(level + 1, m - level):
                result.append(matrix[i][n - level - 1])
            
            #from right to left
            if m - level - 1 > level:
                for i in range(n - level - 2, level - 1, -1):
                    result.append(matrix[m - level - 1][i])
            
            #from bottom to top
            if n - level - 1 > level:
                for i in range(m - level - 2, level, -1):
                    result.append(matrix[i][level])
            
            level+=1
        return result