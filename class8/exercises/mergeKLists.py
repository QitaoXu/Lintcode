from heapq import heappop, heappush

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if len(lists) == 0 or lists is None:
            
            return None
            
            
        # return self.mergeKListsHelper(lists, 0, len(lists) - 1)
        # return self.heap_method(lists)
        return self.two_merge_method(lists)
    
    #
    # Solution 1: Divide Conquer, similar to merge sort
    #
    def mergeKListsHelper(self, lists, start, end):
        
        if start >= end:
            return lists[start]
            
        left = self.mergeKListsHelper(lists, start, (start + end) // 2)
        right = self.mergeKListsHelper(lists, (start + end) // 2 + 1, end)
        
        return self.merge2Lists(left, right)
    
    
        
    def merge2Lists(self, l1, l2):
        
        l = ListNode(-1)
        
        head = l 
        
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
    #    
    # Solution 2: Take advantage of minHeap
    #
    def heap_method(self, lists):
        
        heap = [] 
        
        counter = 0 
        
        for list_head in lists:
            
            if list_head:
                
                heappush(heap, (list_head.val, counter, list_head))
                
                counter += 1 
                
        l = ListNode(-1)
        
        dummy = l 
        
        while heap:
            
            node = heappop(heap)
            
            l.next = node[2]
            
            l = l.next 
            
            if node[2].next:
                
                counter += 1
                
                heappush(heap, (node[2].next.val, counter, node[2].next))
                
        return dummy.next
        
    #
    # Solution 3: Merge 2 by 2  
    #
    def two_merge_method(self, lists):
        
        
        while len(lists) > 1:
        
            new_lists = []
            
            
            for i in range(0, len(lists), 2):
                if i + 1 >= len(lists):
                    break
                new_list = self.merge2Lists(lists[i], lists[i + 1])
                new_lists.append(new_list)
                
            if len(lists) % 2 == 1:
                new_lists.append(lists[-1])
                
            lists = new_lists
            
        return lists[0]