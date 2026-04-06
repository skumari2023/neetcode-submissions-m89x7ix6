# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None 
        elif max(p.val, q.val) < root.val: 
            return self.lowestCommonAncestor(root.left, p, q) 
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        
        #if the root.val is between p.val and q.val == return root.val
        #elif root.val > max(p,q) --> go to left node
        #elif root.val < min (p,q) --> go to right node