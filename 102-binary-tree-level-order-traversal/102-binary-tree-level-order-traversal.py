# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution(object):
    def levelOrder(self, root):
        
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # OP array 
        res = []
        # Queue for BFS
        q = deque()
        q.append(root)
        
        while q:
            len_q = len(q)
            level = []
            for i in range(len_q):
                node = q.popleft() 
                if(node):
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if(level):     
                res.append(level)
        
        return res
                    
                    
        
        
        
        