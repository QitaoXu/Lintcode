"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        
        if headA == None or headB == None:
            
            return None 
        
        nodeA = headA  
        while nodeA.next != None:
            nodeA = nodeA.next 
    
        nodeA.next = headB 
        
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
                
            return slow
            
            
        else:
            return None 