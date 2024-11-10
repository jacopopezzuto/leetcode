class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=9
        rows=[]
        columns=[]
        square=[]
        for i in range(n):
            rows.append(set())
            columns.append(set())
            square.append(set())
        
        for i in range(n):
            for j in range(n):
                val=board[i][j]
                if val=='.':
                    continue
                if val in rows[i]:
                    return False
                rows[i].add(val)
                
                if val in columns[j]:
                    return False
                columns[j].add(val)
                
                idx=(i//3)*3+j//3
                if val in square[idx]:
                    return False
                square[idx].add(val)
        return True