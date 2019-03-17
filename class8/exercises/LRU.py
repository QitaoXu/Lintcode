class LinkedNode():
    
    def __init__(self, key=None, val=None, next=None):
        self.key = key 
        self.val = val 
        self.next = next 

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self.head = LinkedNode()
        self.tail = self.head
        self.hashTable = {}
        
    def pushBack(self, node):
        
        self.hashTable[node.key] = self.tail
        self.tail.next = node 
        self.tail = self.tail.next 
        
    def popFront(self):
        
        del self.hashTable[self.head.next.key]
        
        self.head.next = self.head.next.next
        
        self.hashTable[self.head.next.key] = self.head
    
    def kick(self, prev):
        
        node = prev.next 
        
        if node == self.tail:
            return 
        
        prev.next = node.next 
        
        if node.next is not None:
            
            self.hashTable[node.next.key] = prev
            node.next = None 
            
        self.pushBack(node)

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if not key in self.hashTable:
            return -1 
            
        prev = self.hashTable[key] 
        
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
        
        if key in self.hashTable:
            
            self.kick(self.hashTable[key])
            self.hashTable[key].next.val = value
            
        else:
            
            node = LinkedNode(key, value)
            self.pushBack(node)
            if len(self.hashTable) > self.capacity:
                self.popFront()