"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        mp = {}

        #forgot to use dfs function
        def dfs(node):
            if node in mp:
                return mp[node]
            
            copy = Node(node.val)
            mp[node] = copy 

            for j in node.neighbors:
                copy.neighbors.append(dfs(j))
            
            return copy
        
        #forgot this check
        if node:
            return dfs(node)
        else:
            return None