/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

class ListNode {

    int val; 
    ListNode next; 
    ListNode (int x) {
        val = x; 
    }
}
public class ReverseNodesInKGroup {
    public ListNode reverseKGroup(ListNode head, int k) {
        
        if (head == null || k <= 1) return head;
        
        ListNode dummy = new ListNode(-1); 
        dummy.next = head; 
        head = dummy; 
        
        while (head.next != null) {
            
            head = reverseNextK(head, k);
        }
        
        return dummy.next;
        
    }
    
    private ListNode reverseNextK(ListNode head, int k) {
        
        ListNode next = head; 
        
        for (int i = 0; i < k; i++) {
            
            if (next.next == null) {
                return next;
            }
            
            next = next.next;
        }
        
        ListNode n1 = head.next; 
        ListNode prev = head; 
        ListNode curt = n1; 
        
        for (int i = 0; i < k; i++) {
            ListNode temp = curt.next; 
            curt.next = prev; 
            prev = curt;
            curt = temp; 
        }
        
        n1.next = curt;
        head.next = prev;
        
        return n1;
    }
}