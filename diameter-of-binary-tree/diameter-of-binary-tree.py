# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  
    def HeightOfBinaryTree(self, root ,ans):
      
      if root is None:
        return 0
      
      lh = self.HeightOfBinaryTree(root.left , ans)
      rh = self.HeightOfBinaryTree(root.right , ans)
      
      ans[0] = max(ans[0] , 1 + rh + lh)
      
      return 1 + max(lh,rh)
      
      
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
      if root == None:
        return 0
      ans = [-10]
      heightOfTree = self.HeightOfBinaryTree(root , ans)
      return ans[0] - 1
        