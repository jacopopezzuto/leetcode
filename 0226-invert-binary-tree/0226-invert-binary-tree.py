# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
            
        help_root = root.right
        root.right = root.left
        root.left = help_root
        
        self.invertTree(root.right)
        self.invertTree(root.left)
        
        return root