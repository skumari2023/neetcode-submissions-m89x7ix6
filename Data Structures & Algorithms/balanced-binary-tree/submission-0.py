# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        def maxHeight(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            return 1 + max(maxHeight(node.left), maxHeight(node.right))
        
        #do not need to use self. for a local class
        maxLeft = maxHeight(root.left)
        maxRight = maxHeight(root.right)
        maxHeight = max(maxLeft, maxRight)
        minHeight = min(maxLeft, maxRight)
        
        #first condition just checks root must check left and right
        if maxHeight - minHeight <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        
        return False
        

