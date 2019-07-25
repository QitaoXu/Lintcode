import java.util.*;

class MyQueue {
    
    private Stack<Integer> stack1;
    private Stack<Integer> stack2;

    /** Initialize your data structure here. */
    public MyQueue() {
        
        this.stack1 = new Stack<Integer>();
        this.stack2 = new Stack<Integer>();
        
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) {
        
        stack1.push(x);
        
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        
        if (stack2.isEmpty()) {
            
            this.stack1ToStack2();
        }
        
        return stack2.pop();
        
    }
    
    private void stack1ToStack2() {
        
        while (!stack1.isEmpty()) {
            
            stack2.push(stack1.pop());
        }
    }
    
    /** Get the front element. */
    public int peek() {
        
        if (stack2.isEmpty()) {
            this.stack1ToStack2();
        }
        
        return stack2.peek();
        
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        
        return (stack1.isEmpty() && stack2.isEmpty());
        
    }
}