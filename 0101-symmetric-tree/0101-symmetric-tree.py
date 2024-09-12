# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def checkIsSymmetric(left,right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val == right.val:
                outPair=checkIsSymmetric(left.left,right.right)
                inPair=checkIsSymmetric(left.right,right.left)
                return outPair and inPair
            else:
                return False
        return checkIsSymmetric(root.left,root.right)
        