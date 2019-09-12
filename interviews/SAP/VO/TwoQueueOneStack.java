import java.util.Queue; 
import java.util.LinkedList; 

public class Stack {
    
    private Queue<Integer> queue1;
    private Queue<Integer> queue2;
    
    public Stack() {
        queue1 = new LinkedList<Integer>();
        queue2 = new LinkedList<Integer>();
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
    /*
     * @param x: An integer
     * @return: nothing
     */
    public void push(int x) {
        // write your code here
        queue1.offer(x);
    }

    /*
     * @return: nothing
     */
    public void pop() {
        // write your code here
        moveItems();
        queue1.poll();
        swapQueues();
    }

    /*
     * @return: An integer
     */
    public int top() {
        // write your code here
        moveItems();
        int item = queue1.poll();
        swapQueues();
        queue1.offer(item);
        return item;
    }

    /*
     * @return: True if the stack is empty
     */
    public boolean isEmpty() {
        // write your code here
        return queue1.isEmpty();
    }
}