# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def countPaths(node: Optional[TreeNode], targetSum: int) -> int:
            if node is None:
                return 0

            count = 1 if node.val == targetSum else 0
            count += countPaths(node.left, targetSum - node.val)
            count += countPaths(node.right, targetSum - node.val)

            return count
        
        if root is None:
            return 0
        
        count = countPaths(root, targetSum)
        count += self.pathSum(root.left, targetSum)
        count += self.pathSum(root.right, targetSum)
        
        return count
       
        