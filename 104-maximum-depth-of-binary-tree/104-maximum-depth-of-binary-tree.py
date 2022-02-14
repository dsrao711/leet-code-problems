# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        q = deque()
        q.append(root)
        level = 0
        
        if(root == None):
            return 0 
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if(node):
                    if(node.left):
                        q.append(node.left)
                    if(node.right):
                        q.append(node.right)
                    
            level += 1
        
        return level