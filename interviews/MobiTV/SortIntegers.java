import java.util.*; 

public class SortIntegers {
    /**
     * @param A: an integer array
     * @return: nothing
     */
    public void sortIntegers(int[] A) {
        // write your code here
        
        if (A == null || A.length == 0) {
            return;
        }
        
        int[] temp = new int[A.length];
        
        this.mergeSort(A, 0, A.length - 1, temp);
        
        this.quickSort(A, 0, A.length - 1);
    }
    
    private void quickSort(int[] nums, int start, int end) {
        
        if (start >= end) {
            return;
        }
        
        int pivot = nums[start + (end - start) / 2]; 
        int left = start, right = end; 
        
        while (left <= right) {
            
            while (left <= right && nums[left] < pivot) {
                left += 1;
            } 
            
            while (left <= right && nums[right] > pivot) {
                right -= 1;
            }
            
            if (left <= right) {
                
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                left += 1;
                right -= 1;
            }
        }
        
        this.quickSort(nums, start, right);
        this.quickSort(nums, left, end);
    }
    
    private void mergeSort(int[] nums, int start, int end, int[] temp) {
        
        if (start >= end) {
            
            return;
        }
        
        int mid = start + (end - start) / 2; 
        
        this.mergeSort(nums, start, mid, temp);
        this.mergeSort(nums, mid + 1, end, temp);
        
        this.mergeSortHelper(nums, start, end, temp);
     }
     
     private void mergeSortHelper(int[] nums, int start, int end, int[] temp) {
         
         int mid = start + (end - start) / 2; 
         
         int left = start, right = mid + 1; 
         
         int index = start;
         
         while (left <= mid && right <= end) {
             
             if (nums[left] <= nums[right]) {
                 temp[index] = nums[left];
                 left += 1;
                 index += 1;
             }
             
             else {
                 temp[index] = nums[right];
                 right += 1;
                 index += 1;
             }
             
         }
         
         while (left <= mid) {
             
             temp[index] = nums[left];
             left += 1;
             index += 1;
         }
         
         while (right <= end) {
             temp[index] = nums[right];
             right += 1;
             index += 1;
         }
         
         for (int i = start; i <= end; i++) {
             nums[i] = temp[i];
         }
     }
}