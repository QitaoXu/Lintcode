class LinkedNode:
    
    def __init__(self, key = None, value = None, next = None, ttl = None): 
        self.key = key 
        self.value = value 
        self.next = next 
        self.ttl = ttl 

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        
        self.key_to_prev = {} 
        self.head = LinkedNode()
        self.tail = self.head  
        self.capacity = capacity 
        
    def pop_front(self):
        
        del self.key_to_prev[self.head.next.key]
        
        self.head.next = self.head.next.next 
        
        self.key_to_prev[self.head.next.key] = self.head 
        
    def push_back(self, node):
        
        self.key_to_prev[node.key] = self.tail 
        
        self.tail.next = node 
        
        self.tail = self.tail.next 

    def serialize(self):
        pass 

    def deserialize(self):
        pass 
        
    
    # head -> ... -> prev -> node -> node.next -> ... -> None 
    # head -> ... -> prev -> node.next ... -> node -> None 
    def kick(self, prev):
        
        node = prev.next 
        
        if node == self.tail:
            return 
        
        prev.next = node.next 
        
        if prev.next is not None:
            
            self.key_to_prev[node.next.key] = prev 
            
            node.next = None 
            
        self.push_back(node)
        
    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        
        if key not in self.key_to_prev:
            return -1 
        
        prev = self.key_to_prev[key]
        
        node = prev.next 
        
        self.kick(prev)
        
        return node.value

    """
    @param: keys: An integer list 
    @return: An integer list 
    """

    def getMultiple(self, keys):

        values = [] 

        for key in keys:

            values.append(self.get(key)) 

        return values 
        

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value, ttl):
        
        if key in self.key_to_prev: 
            
            prev = self.key_to_prev[key]
            
            self.kick(prev)
            
            self.key_to_prev[key].next.value = value 
            self.key_to_prev[key].ttl = ttl 
            
        else:
            
            node = LinkedNode(key = key, value = value, ttl = ttl) 
            
            self.push_back(node)
            
            if len(self.key_to_prev) > self.capacity:
                
                self.pop_front()

    """
    @param: keys: An integer list
    @param: values: An integer list
    @return: nothing
    """
    def setMultiple(self, keys, values, ttls):

        for index in range(len(keys)):

            key, value, ttl = keys[index], values[index], ttls[index]

            self.set(key, value, ttl)  

    """
    @param: keys: An integer
    @return: nothing
    """
    def delete(self, key):

        if key not in self.key_to_prev:
            return False

        prev = self.key_to_prev[key] 

        prev.next = prev.next.next 

        del self.key_to_prev[key] 

        # deleted node is not last node 
        if prev.next is not None:

            self.key_to_prev[prev.next.key] = prev 

        # deleted node is last node 
        else:

            self.tail = prev 

        return True 


