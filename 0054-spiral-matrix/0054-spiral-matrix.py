class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        min_columns, min_rows = 0, 0
        max_column, max_rows = len(matrix[0]), len(matrix)
        while max_column>min_columns and max_rows>min_rows:
            for j in range(min_columns, max_column):
                result.append(matrix[min_rows][j])
            min_rows+=1
            for i in range(min_rows,max_rows):
                result.append(matrix[i][max_column-1])
            max_column-=1
            if min_rows < max_rows:
                for j in range(max_column-1,min_columns-1,-1):
                    result.append(matrix[max_rows-1][j])
                max_rows-=1
            if min_columns < max_column:
                for i in range(max_rows-1,min_rows-1,-1):
                    result.append(matrix[i][min_columns])
                min_columns+=1
        return result