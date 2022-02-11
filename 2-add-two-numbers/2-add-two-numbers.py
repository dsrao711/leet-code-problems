# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # 1. Traverse till the either ll1 or ll2 is not null
        # Create p1 to point to ll1 , p2 -> ll2 , res -> dummy
        # 2. Create a dummy head to store the res
        # 3. Carry variable to store carry
        # 4. sum =  node1.val + node2.val  + carry 
        # 5. carr = sum / 10
        # 6. res.val = sum % 10
        # 7. Advance res 
        # 8. Advance p1 and p2 till not null
        
        dummy = ListNode()
        head1 = l1
        head2 = l2
        curr = dummy 
        carry = 0
        
        while(head1 or head2):
            if(head1 is not None):
                x = head1.val
            else:
                x = 0
                
            if(head2 is not None):
                y = head2.val
            else:
                y = 0 
            # calc sum of lsbs nd carry    
            add = x + y + carry
            carry = add/10
            curr.next = ListNode(add % 10)
            curr = curr.next
            
            if(head1 is not None):
                head1 = head1.next
                
            if(head2 is not None):
                head2 = head2.next
                
        # Last carry if present any    
        if(carry > 0):
            curr.next = ListNode(carry)
            
        return dummy.next
            