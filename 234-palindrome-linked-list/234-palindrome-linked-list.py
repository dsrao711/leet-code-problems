# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        # p1 = first 
        # p2 = last -> for storing lst nodes  use a stack
        # traverse till mid
        # check if p1 == p2
        # if not break
        
        stack = []
        temp = head
        while(temp):
            stack.append(temp.val)
            temp = temp.next
            
        # find mid 
        curr = head
        counter = 0
        while(curr):
            counter += 1
            curr = curr.next
            
        mid = counter // 2
        
        p1 = head
        p2 = stack.pop()
        
        while(mid):
            if(p1.val != p2):
                return False
            p1 = p1.next
            p2 = stack.pop()
            mid -= 1
            
        return True
            
        