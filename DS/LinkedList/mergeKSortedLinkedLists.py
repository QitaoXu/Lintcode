# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists):
        
        if not lists:
            return None 
        
        # return self.mergeKListsHelper(lists, 0, len(lists) - 1)
        
        # return self.mergeByHeap(lists)
        
        return self.mergeTwoByTwo(lists)
    
    def mergeKListsHelper(self, lists, start, end):
        
        if start >= end:
            return lists[start]
        
        mid = start + (end - start) // 2 
        
        left = self.mergeKListsHelper(lists, start, mid) 
        right = self.mergeKListsHelper(lists, mid + 1, end) 
        
        return self.mergeTwoLists(left, right) 
    
    def mergeTwoLists(self, l1, l2):
        
        head = ListNode(-1) 
        
        l = head 
        
        while l1 is not None and l2 is not None:
            
            if l1.val < l2.val:
                
                l.next = l1
                l = l.next 
                l1 = l1.next 
                
            else:
                l.next = l2
                l = l.next 
                l2 = l2.next 
                
        while l1 is not None:
            
            l.next = l1
            l = l.next 
            l1 = l1.next 
            
        while l2 is not None:
            
            l.next = l2
            l = l.next 
            l2 = l2.next 
            
        return head.next 
        
     
    
    def mergeTwoByTwo(self, lists):
        
        while len(lists) > 1:
            
            new_lists = [] 
            
            for i in range(0, len(lists), 2):
                
                if i + 1 >= len(lists):
                    break 
                    
                new_list = self.mergeTwoLists(lists[i], lists[i + 1])
                new_lists.append(new_list) 
                
            if len(lists) % 2 == 1:
                new_lists.append(lists[-1])
                
            lists = new_lists
                
        return lists[0] 
        
        
        
    def mergeByHeap(self, lists):
        
        heap = [] 
        counter = 1 
        
        for i in range(len(lists)):
            
            head = lists[i]
            
            if head is not None:
            
                heappush(heap, (head.val, counter, head)) 
                counter += 1 
            
            
        dummy = ListNode(-1) 
        l = dummy 
        
        while heap:
            
            _, _, node = heappop(heap) 
            
            l.next = node 
            l = l.next 
            
            node = node.next 
            
            if node:
                
                heappush(heap, (node.val, counter, node))
                
                counter += 1 
                
        return dummy.next 
            
            
        
    