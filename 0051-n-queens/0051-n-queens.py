class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        empty_board=[]
        for i in range(n):
            empty_board.append(["."]*n)
        self.backtrack(0, set(), set(), set(), empty_board,n,ans)
        return ans
    
    def create_board(self, state):
        board=[]
        for row in state:
            board.append("".join(row))
        return board
    
    def backtrack(self, row, diagonals, anti_diagonals, cols, state,n, ans):
        if row==n:
            ans.append(self.create_board(state))
            return
        for col in range(n):
            curr_diagonal=row-col
            curr_anti_diagonal = row+col
            if(col in cols or curr_diagonal in diagonals or curr_anti_diagonal in anti_diagonals):
                continue
            cols.add(col)
            diagonals.add(curr_diagonal)
            anti_diagonals.add(curr_anti_diagonal)
            state[row][col]="Q"
            
            self.backtrack(row+1, diagonals, anti_diagonals, cols, state,n,ans)
            
            cols.remove(col)
            diagonals.remove(curr_diagonal)
            anti_diagonals.remove(curr_anti_diagonal)
            state[row][col]="."
            
    
    