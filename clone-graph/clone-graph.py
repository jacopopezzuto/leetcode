"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited={}
        def dfs(node):
            if not node:
                return None
            if not node.neighbors:
                return Node(node.val)
            if node in visited:
                return visited[node]
            if node not in visited:
                newNode=Node(node.val)
                visited[node]=newNode
                for item in node.neighbors:
                    newNode.neighbors.append(dfs(item))
                return newNode
            
        root=dfs(node)
        return root