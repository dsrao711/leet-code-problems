# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def insert(root,x):
          if(root):
            if(x < root.val):
              # Insert Left
              # If Left node is already present
              if(root.left):
                insert(root.left,x)        
              #Else, create a new left node
              else:
                root.left = TreeNode(x)
            else:
              # Insert Right
              # If Right node is already present
              if(root.right):
                insert(root.right , x)
              # Else , create a new right node
              else:
                root.right = TreeNode(x)
                
          else:
            return root
            
        if not root:
          return TreeNode(val)
        
        insert(root , val)
        
        return root
                
              
          