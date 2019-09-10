class LinkedNode {
    
    int key; 
    int value; 
    LinkedNode next; 
    
    public LinkedNode(int key, int value) {
        
        this.key = key;
        this.value = value; 
        this.next = null;
    }
}

public class LRUCache {
    
    Map<Integer, LinkedNode> keyToPrev; 
    LinkedNode head;
    LinkedNode tail;
    int capacity;
    
    /*
    * @param capacity: An integer
    */public LRUCache(int capacity) {
        // do intialization if necessary
        this.keyToPrev = new HashMap<Integer, LinkedNode>();
        this.head = new LinkedNode(-1, -1);
        this.tail = this.head; 
        this.capacity = capacity;
        
    }
    
    private void popFront() {
        
        this.keyToPrev.remove(this.head.next.key);
        this.head.next = this.head.next.next;
        this.keyToPrev.put(this.head.next.key, this.head); 
    }
    
    private void pushBack(LinkedNode node) {
        
         
        this.keyToPrev.put(node.key, this.tail); 
        this.tail.next = node;
        this.tail = this.tail.next;
    }
    
    private void kick(LinkedNode prev) {
        
        LinkedNode node = prev.next;
        if (node == this.tail) 
            return;
            
        prev.next = node.next; 
        
        if (node.next != null) {
            
            this.keyToPrev.put(node.next.key, prev);
            node.next = null;
        }
        
        this.pushBack(node);
    }
    
    
    /*
     * @param key: An integer
     * @return: An integer
     */
    public int get(int key) {
        // write your code here
        
        if (!this.keyToPrev.containsKey(key)) {
            return -1; 
        }
        
        LinkedNode prev = this.keyToPrev.get(key); 
        LinkedNode node = prev.next;
        
        this.kick(prev);
        return node.value;
    }

    /*
     * @param key: An integer
     * @param value: An integer
     * @return: nothing
     */
    public void set(int key, int value) {
        // write your code here
        
        if (this.keyToPrev.containsKey(key)) {
            
            LinkedNode prev = this.keyToPrev.get(key);
            
            this.kick(prev);
            this.keyToPrev.get(key).next.value = value;
            
        }
        
        else {
            
            LinkedNode node = new LinkedNode(key, value); 
            
            this.pushBack(node);
            
            if (this.keyToPrev.size() > this.capacity) {
                this.popFront();
            }
        }
        
    }
}