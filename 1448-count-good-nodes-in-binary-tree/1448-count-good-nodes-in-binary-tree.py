# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def good(root:TreeNode, max_val:int):
            if root is None:
                return 0
            if root.val>=max_val:
                max_val=root.val
                count=1
            else:
                count=0
            count+=good(root.left,max_val)
            count+=good(root.right,max_val)
            return count
        return good(root,root.val)