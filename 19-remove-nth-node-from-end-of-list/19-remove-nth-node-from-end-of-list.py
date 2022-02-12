# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        dummyhead = ListNode()
        dummyhead.next = head
        fast = dummyhead
        slow = dummyhead
        
        for i in range(0 , n):
            fast = fast.next
            
        while(fast.next):
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next
        
        return dummyhead.next
            