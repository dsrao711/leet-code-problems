# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        stack = []
        prev = None
        
        while stack or root : 
            # left
            while root :
                stack.append(root)
                root = root.left
            root = stack.pop()
            # Inorder
            if(prev and prev.val >= root.val):
                return False
            prev = root
            # right
            root = root.right
            
        return True
            