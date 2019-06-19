# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        if headA is None or headB is None:
            return None 
        
        node = headA 
        
        while node.next is not None:
            
            node = node.next 
            
        node.next = headB 
        
        slow, fast = headA, headA
        
        while fast != None and fast.next != None:
            
            slow = slow.next 
            fast = fast.next.next 
            
            if slow == fast:
                break 
                
        if slow == fast:
            
            slow = headA
                
            while slow != fast:
                slow = slow.next 
                fast = fast.next 
                
            node.next = None        
            return slow 
            
        else:
            
            node.next = None 
            return None 