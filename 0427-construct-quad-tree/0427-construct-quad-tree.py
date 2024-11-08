"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def solve(n,r,c):
            is_equal=True
            for i in range(n):
                for j in range(n):
                    if grid[r][c]!=grid[r+i][c+j]:
                        is_equal=False
                        break
                if not is_equal: break
            if is_equal==True:
                return Node(grid[r][c],1)
            n=n//2
            top_left=solve(n,r,c)
            top_right=solve(n,r,c+n)
            bottom_left=solve(n,r+n,c)
            bottom_right=solve(n,r+n,c+n)
            return Node(grid[r][c],0,top_left,top_right,bottom_left,bottom_right)
                    
        return solve(len(grid), 0,0)