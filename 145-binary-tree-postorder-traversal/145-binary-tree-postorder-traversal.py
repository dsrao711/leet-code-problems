# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        op = []
        stack = []
        
        curr = root
        
        while(stack or curr):
            
            if(curr):
                stack.append(curr)
                curr = curr.left
                
            else:
                temp = stack[-1].right
                if(temp == None):
                    temp = stack[-1]
                    stack.pop()
                    op.append(temp.val)
                    while(stack and temp == stack[-1].right):
                        temp = stack[-1]
                        stack.pop()
                        op.append(temp.val)
                else:
                    curr = temp
                    
        return op
                