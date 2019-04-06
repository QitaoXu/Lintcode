"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        
        if not head:
            
            return head 
            
        # clone node after original node 
        # A->B->C => A->A'->B->B'->C->C'
        
        ptr = head 
        
        while ptr:
            
            new_node = RandomListNode(ptr.label)
            
            new_node.next = ptr.next 
            
            ptr.next = new_node
            
            ptr = new_node.next 
            
        # clone random 
        
        ptr = head 
        
        while ptr:
            
            ptr.next.random = ptr.random.next if ptr.random else None 
            
            ptr = ptr.next.next 
        
        # de-weave    
        old_list_tail = head 
        new_list_tail = head.next 
        
        new_list_head = head.next 
        
        while new_list_tail:
            
            old_list_tail.next = new_list_tail.next 
            new_list_tail.next = new_list_tail.next.next if new_list_tail.next else None 
            
            old_list_tail = old_list_tail.next 
            new_list_tail = new_list_tail.next 
            
        return new_list_head