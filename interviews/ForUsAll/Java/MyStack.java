import java.util.*;
class MyStack {
    
    private Queue<Integer> queue1;
    private Queue<Integer> queue2;

    /** Initialize your data structure here. */
    public MyStack() {
        
        this.queue1 = new LinkedList<Integer>();
        this.queue2 = new LinkedList<Integer>();
        
    }
    
    private void moveItems() {
        
        while (queue1.size() != 1) {
            
            queue2.offer(queue1.poll());
        }
    }
    
    private void swapQueues() {
        
        Queue<Integer> temp = queue1; 
        queue1 = queue2;
        queue2 = temp;
    }
    
    /** Push element x onto stack. */
    public void push(int x) {
        
        queue1.offer(x);
        
    }
    
    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        
        this.moveItems();
        
        int item = queue1.poll();
        
        this.swapQueues();
        
        return item;
        
        
    }
    
 
    
    /** Get the top element. */
    public int top() {
        
        this.moveItems(); 
        
        int item = queue1.poll();
        
        queue2.offer(item);
        
        this.swapQueues();
        
        return item;
        
    }
    
    /** Returns whether the stack is empty. */
    public boolean empty() {
        
        return queue1.isEmpty();
        
    }
}
