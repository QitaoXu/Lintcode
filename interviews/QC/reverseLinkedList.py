# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        
        return self.revereListHelper(head, None)
    
    def revereListHelper(self, start, end):
        
        prev = None
        curr = start
        
        while curr != end:
            
            nextTemp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = nextTemp 
            
        return prev 
        