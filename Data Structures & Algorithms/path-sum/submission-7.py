# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node,pathS):
            
            if not node:
                return False
            
            pathS += node.val 

            if not node.right and not node.left:
                return targetSum == pathS

            return dfs(node.left,pathS) or dfs(node.right,pathS)

        return dfs(root,0)