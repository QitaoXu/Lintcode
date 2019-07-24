import java.util.ArrayList;

class ComputeTarget {

    public boolean canComputeTarget(ArrayList<Integer> nums, int target) {

        return false;
    }

    private dfs(ArrayList<Integer> nums, 
                int index, 
                int curt, 
                int target) {

        if (curt == target) return true; 

        if (index == nums.size()) return false;

        if (this.dfs(nums, index + 1, curt + nums.get(index), target)) 
                return true;

        if (this.dfs(nums, index + 1, curt * nums.get(index), target)) 
                return true;

        return false;
    }
}