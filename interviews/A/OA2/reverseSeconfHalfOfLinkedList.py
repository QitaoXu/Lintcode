class ListNode:

    def __init__(self, val):
        self.val = val 
        self.next = None 

class Solution:

    def reverseSecondHalfOfLinkedList(self, head):

        if not head or not head.next:
            return head 

        slow = head
        fast = head 

        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next 
            slow = slow.next 

        pre = slow.next 
        cur = pre.next 

        # slow->pre->cur 

        while cur is not None:

            pre.next = cur.next 
            cur.next = slow.next 
            slow.next = cur
            cur = pre.next 

        return head 