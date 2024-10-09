# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        level, max_sum, max_level = 1, float('-inf'), 1
        while queue:
            nodes = len(queue)
            level_sum = 0
            for i in range(0,nodes):
                node = queue.popleft()
                level_sum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level_sum > max_sum:
                max_sum=level_sum
                max_level = level
            level+=1
        return max_level