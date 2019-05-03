from heapq import heappush, heappop
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        
        # Solution1: divide conquer, similar 
        # return self.divide_conquer(lists)
        
        # Solution2: merge 2 by 2 
        # return self.merge2by2(lists)
        
        # Solution3: heap 
        return self.mergeByHeap(lists)
        
    def divide_conquer(self, lists):
        if not lists:
            return None 
        
        start, end = 0, len(lists) - 1 
        return self.mergeKListsHelper(lists, start, end)
    
    def mergeKListsHelper(self, lists, start, end):
        
        
        if start >= end:
            return lists[start]
            
        mid = start + (end - start) // 2 
            
        left = self.mergeKListsHelper(lists, start, mid)
        right = self.mergeKListsHelper(lists, mid + 1, end)
        
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
        
    def merge2by2(self, lists):
        
        if not lists:
            return None 
        
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
    
    def mergeByHeap(self, lists):
        
        if not lists:
            return None 
        
        heap = [] 
        counter = 0 
        
        for list_head in lists:
            
            if list_head:
                
                heappush(heap, (list_head.val, counter, list_head))
                
                counter += 1 
                
        l = ListNode(-1)
        dummy = l 
                
        while heap:
            
            _, __, node = heappop(heap)
            
            l.next = node 
            l = l.next 
            
            node = node.next 
            
            if node:
                counter += 1 
                heappush(heap, (node.val, counter, node))
                
        return dummy.next 
                
                
        

