import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;

public class NumDiff {

    public static void main(String[] args) {

        int[] nums = {4, 6, 8, 9};
        int k = 2;
        int m = 3; 

        Solution solution = new Solution();

        System.out.println(solution.findNumsDiff(nums, k, m));

    }
}

class Solution{

    public List<Integer> findNumsDiff(int[] nums, int k, int m) {

        HashMap<Integer, List<Integer>> modToNums = new HashMap<>(); 

        for (Integer num : nums) {

            int mod = num % k; 

            if (!modToNums.containsKey(mod)) {
                modToNums.put(mod, new ArrayList<Integer>());
            }

            modToNums.get(mod).add(num);
        }

        for (Integer key : modToNums.keySet()) {

            if (modToNums.get(key).size() == m ) return modToNums.get(key);
        }

        return new ArrayList<Integer>();
    }



}