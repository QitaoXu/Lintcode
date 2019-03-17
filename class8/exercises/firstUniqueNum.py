class DataStream:

    def __init__(self):
        # do intialization if necessary
        self.dummy = ListNode(0)
        self.tail = self.dummy 
        self.num_to_prev = {}
        self.duplicates = set()
        
          
    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        # write your code here
        
        if num in self.duplicates:
            
            return 
        
        prev = self.num_to_prev.get(num)
        
        if prev is not None:
            
            self.duplicates.add(num)
            
            del self.num_to_prev[num]
            
            prev.next = prev.next.next 
            
            if prev.next is not None:
                
                self.num_to_prev[prev.next.val] = prev
                
            else:
                self.tail = prev 
                
            return 
        
        node = ListNode(num)
        
        self.tail.next = node 
        
        self.num_to_prev[num] = self.tail
        
        self.tail = self.tail.next
            
            

    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        # write your code here
        
        if self.dummy.next is not None:
            
            return self.dummy.next.val
            
        return -1 



class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        # Write your code here
        
        ds = DataStream()
        
        for i in range(len(nums)):
            
            ds.add(nums[i])
            
            if nums[i] == number:
                
                return ds.firstUnique()
            
        return -1