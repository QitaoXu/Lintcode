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
public class ReverseLinkedList {
    public ListNode reverseList(ListNode head) {
        
        ListNode prev = null; 
        ListNode curr = head; 
        
        while (curr != null) {
            
            ListNode next = curr.next; 
            curr.next = prev;
            prev = curr; 
            curr = next;
        }
        
        return prev;
        
    }
}