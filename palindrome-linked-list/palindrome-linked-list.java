/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        
        if (head == null ){
            return true ;
        }
        
        ListNode fast = head ;
        ListNode slow = head ;
        
        while(fast.next != null && fast.next.next != null){
            fast = fast.next.next ;
            slow = slow.next ;
            
        }
        ListNode secondhalf_head = reverse(slow.next) ;
        ListNode firsthalf_head = head ;
        
        while(firsthalf_head != null && secondhalf_head != null){
            if(firsthalf_head.val != secondhalf_head.val){
                return false ;
            }
            
            firsthalf_head = firsthalf_head.next ;
            secondhalf_head = secondhalf_head.next ;
            
        }
        return true ;
    }
        
        private ListNode reverse (ListNode head){
            ListNode newHead = null ;
            while(head != null) {
                ListNode temp = head.next; 
                head.next = newHead ;
                newHead = head ;
                head = temp ;
            }
            return newHead ;
        }
    }
