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
    @param l1: The first list.
    @param l2: The second list.
    @return: the sum list of l1 and l2.
    """
    def addLists2(self, l1, l2):
        # write your code here
        
        num1 = self.list_to_num(l1)
        num2 = self.list_to_num(l2)
        
        num = num1 + num2 
        
        digits = self.num_to_digits(num)
        
        l = self.digits_to_list(digits)
        
        return l 
        
    def list_to_num(self, head):
        
        num = 0 
        
        while head:
            
            num = num * 10 + head.val 
            
            head = head.next 
            
        return num 
        
    def num_to_digits(self, num):
        
        if num == 0:
            
            return [0]
            
        digits = []
            
        while num > 0:
            
            digit = num % 10 
            
            digits.append(digit)
            
            num = num // 10 
            
        digits.reverse()
        
        return digits
        
    def digits_to_list(self, digits):
        
        head = ListNode(-1)
        
        tail = head 
        
        for digit in digits:
            
            node = ListNode(digit)
            
            tail.next = node 
            
            tail = tail.next 
            
        return head.next 
            
            
            
            
            
            
            
            
            
            
            
            
