# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        q = []
        q.append(root)
        
        while(q):
            node = q.pop(0)
            if(node):
                node.right , node.left = node.left , node.right
                q.append(node.left)
                q.append(node.right)
                
        return root
                