import java.util.*; 

public class RotateArray {

    public void rotateArray(int[] nums) {

        if (nums == null || nums.length == 0)
            return; 

        int start = 0, end = nums.length - 1; 

        while (start < end) {

            int temp = nums[start]; 
            nums[start] = nums[end];
            nums[end] = temp; 
            start += 1;
            end -= 1;
        }
    }
}