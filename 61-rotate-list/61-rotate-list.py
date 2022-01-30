# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        curr = head
        if(curr == None or curr.next == None or k <= 0):
            return head
        # 1. Find the length 
        n = 1
        while(curr.next != None):
            n += 1
            curr = curr.next
        # Point the tail to curr head
        curr.next = head
        # For any k , we need to remove the last k ele and point to front
        # for k > n , we generalize 
        # 2. k = k % n
        k = k % n 
        k = n - k
        # Traverse till n-k and break the connection 
        while(k):
            curr = curr.next
            k -= 1
        # Atatch the remaining nodes  to the head
        head = curr.next
        # and last node to null  
        curr.next = None
        
        return head