# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        # 1. Iterate reverse and store address of each node in a stack 
        # 2. Iterate again and for odd nodes , change and append top of stack 
        
        curr = head
        # Stack
        reverse_order = []
        
        while(curr):
            reverse_order.append(curr.val)
            curr = curr.next
        original_order = reverse_order[::-1]
        
        node = head
        counter = 0
        
        while(node):
            if(counter % 2 == 0):
                node.val = original_order.pop()
            else:
                node.val = reverse_order.pop()
            node = node.next
            counter += 1
            
