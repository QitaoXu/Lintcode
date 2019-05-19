class LinkedNode:
    
    def __init__(self, key=None, val=None, next=None):
        self.key = key 
        self.val = val 
        self.next = next 

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        
        self.capacity = capacity
        
        self.head = LinkedNode()
        
        self.tail = self.head
        
        self.key_to_prev = {}
        
    def popFront(self):
        
        del self.key_to_prev[self.head.next.key]
        
        self.head.next = self.head.next.next 
        
        self.key_to_prev[self.head.next.key] = self.head 
        
    def pushBack(self, node):
        
        self.key_to_prev[node.key] = self.tail 
        
        self.tail.next = node 
        
        self.tail = self.tail.next 
        
    def kick(self, prev):
        
        node = prev.next 
        
        if node == self.tail:
            
            return 
        
        prev.next = node.next 
        
        if prev.next is not None:
            
            self.key_to_prev[prev.next.key] = prev 
            
            node.next = None 
            
        self.pushBack(node)
            
        
        
        

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        
        if key not in self.key_to_prev:
            
            return -1 
            
        prev = self.key_to_prev[key] 
        
        node = prev.next 
        
        self.kick(prev)
        
        return node.val
        
        

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        
        if key in self.key_to_prev:
            
            prev = self.key_to_prev[key]
            
            self.kick(prev)
            
            self.key_to_prev[key].next.val = value 
            
        else:
            
            node = LinkedNode(key, value)
            
            self.pushBack(node)
            
            if len(self.key_to_prev) > self.capacity:
                
                self.popFront()
        
        
        
            
        
        
        
        
                
