import java.util.*; 

public class MedianOfTwoSortedArrays {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        
        int n = nums1.length + nums2.length; 
        
        if (n % 2 == 0) {
            
            return (this.findKth(nums1, nums2, n / 2) + this.findKth(nums1, nums2, n / 2 + 1)) / 2.0;
        } 
        else {
            return this.findKth(nums1, nums2, n / 2 + 1);
        }
        
    }
    
    private int findKth(int[] nums1, int[] nums2, int k) {
        
        if (nums1.length == 0) return nums2[k - 1]; 
        
        if (nums2.length == 0) return nums1[k - 1]; 
        
        int start = Math.min(nums1[0], nums2[0]); 
        int end = Math.max(nums1[nums1.length - 1], nums2[nums2.length - 1]); 
        
        while (start + 1 < end) {
            
            int mid = start + (end - start) / 2; 
            
            if (countSmallerOrEqual(nums1, mid) + countSmallerOrEqual(nums2, mid) < k) {
                
                start = mid; 
            }
            else {
                
                end = mid;
            }
            
        }
        
        if ( countSmallerOrEqual(nums1, start) + countSmallerOrEqual(nums2, start) >= k) {
                return start;
            }
            
        return end;
    }
    
    private int countSmallerOrEqual(int[] nums, int num) {
        
        int start = 0, end = nums.length - 1; 
        
        while (start + 1 < end) {
            
            int mid = start + (end - start) / 2; 
            
            if (nums[mid] <= num) {
                start = mid; 
            }
            
            else {
                end = mid;
            }
        }
        
        if (nums[start] > num) {
            return start;
        }
        
        if (nums[end] > num) {
            return end;
        }
        
        return nums.length;
    }
}