import java.util.*; 

public class MaxDiffInSubarray {

    public int getMaxDiffInSubarray(int[] nums, int d) {

        int left = 0, right = d - 1; 

        int maxDiff = 0; 

        for (int i = 0; i < d - 1; i++) {

            for (int j = 1; j < d; j++) {

                if (Math.abs(nums[i] - nums[j]) > maxDiff) {

                    maxDiff = Math.abs(nums[i] - nums[j]);
                }
            }
        }

        for (int i = 1; i < nums.length - d; i++) {

            int j = i + d - 1;

        }


        return 0;

    }
}