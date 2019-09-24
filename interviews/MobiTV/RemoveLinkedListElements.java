/**
 * Definition for singly-linked list.
 public class ListNode {
      int val;
      ListNode next;
      ListNode(int x) { val = x; }
 }
 */
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

public class RemoveLinkedListElements {
    public ListNode removeElements(ListNode head, int val) {
        
        ListNode curt = head;
        
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        
        ListNode prev = dummy;
        
        while (curt != null) {
            
            if (curt.val == val) {
                
                prev.next = curt.next;
                curt = curt.next;
                continue;
            }
            
            prev = curt;
            curt = curt.next;
        }
        
        return dummy.next;
        
    }
}