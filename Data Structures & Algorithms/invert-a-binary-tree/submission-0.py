# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #check if tree is empty 
        if not root:
            return 
        
        queue = deque([root])
        
        #keep looping until queue is empty 
        while queue:
            
            node = queue.popleft()

            node.right, node.left = node.left, node.right #for swapping
            
            if node.left: #for travesal 
                queue.append(node.left)
            
            if node.right: #for travesal 
                queue.append(node.right)
        
        return root
        