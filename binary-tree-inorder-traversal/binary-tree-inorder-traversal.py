# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
      
      op = []
      stack = deque()

      curr = root

      while stack or curr:

          if curr:
              stack.append(curr)
              curr = curr.left
          else:
              curr = stack.pop()
              op.append(curr.val)
              curr = curr.right
              
      return op