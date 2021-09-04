# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Join 2 linked list
        # Sort the final list
        
        res = ListNode()
        p = res
        
        while(l1 and l2):
          if(l1.val < l2.val):
            p.next = l1
            l1 = l1.next
          else:
            p.next = l2
            l2 = l2.next
            
          p = p.next
          
        if(l1):
          p.next = l1
        else:
          p.next = l2
        
        return res.next
        
        
        
        
        
        
        