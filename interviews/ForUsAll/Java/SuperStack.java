import java.util.*;

public class SuperStack {

    private ArrayList<Integer> nums; 
    private ArrayList<Integer> maxs; 
    private ArrayList<Integer> mins;

    public SuperStack() {

        this.nums = new ArrayList<Integer>();
        this.maxs = new ArrayList<Integer>();
        this.mins = new ArrayList<Integer>();
    }


    public void push(int n) {

        if (nums.size() == 0) {

            nums.add(n);
            maxs.add(n);
            mins.add(n);
        }

        else {

            if (n >= maxs.get(maxs.size() - 1)) {

                nums.add(n);
                maxs.add(n);
                mins.add(mins.get(mins.size() - 1));
            } 
            else if (n <= mins.get(mins.size() - 1)) {

                nums.add(n);
                maxs.add(maxs.get(maxs.size() - 1));
                mins.add(n);
            }
            else {
                nums.add(n);
                maxs.add(maxs.get(maxs.size() - 1));
                mins.add(mins.get(mins.size() - 1));
            }
        }

    }

    public Integer pop() {

        if (nums.size() == 0) return null;

        int ans = nums.get(nums.size() - 1); 
        nums.remove(nums.size() - 1);
        maxs.remove(maxs.size() - 1);
        mins.remove(mins.size() - 1);
        return ans;
    }

    public Integer getMax() {

        if (nums.size() == 0) return null;

        int max = maxs.get(maxs.size() - 1);

        return max;
    }

    public Integer getMin() {

        if (nums.size() == 0) return null;

        int min = mins.get(mins.size() - 1);

        return min;
    }


    
}