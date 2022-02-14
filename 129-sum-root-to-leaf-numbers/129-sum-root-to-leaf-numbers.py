# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def helper(node , path):
            if(not node):
                return
            path = path*10 + node.val
            if(not node.left and not node.right):
                self.add += path
            else:
                helper(node.left , path)
                helper(node.right , path)
              
            
        self.add = 0
        helper(root , 0)
        return self.add