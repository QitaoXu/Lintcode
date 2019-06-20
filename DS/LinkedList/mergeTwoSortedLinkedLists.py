# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        
        head = ListNode(-1) 
        
        l = head
        
        while l1 is not None and l2 is not None: 
            
            if l1.val < l2.val:
                l.next = ListNode(l1.val) 
                l = l.next 
                l1 = l1.next 
                
            else:
                
                l.next = ListNode(l2.val)
                l = l.next 
                l2 = l2.next 
                
        while l1 is not None:
            
            l.next = ListNode(l1.val)
            l = l.next 
            l1 = l1.next 
            
        while l2 is not None:
            
            l.next = ListNode(l2.val)
            l = l.next 
            l2 = l2.next 
            
        return head.next 