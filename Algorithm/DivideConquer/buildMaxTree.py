class TreeNode:

    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None 

class Tree:

    def __init__(self, root):
        self.root = root 

    def inOrder(self):

        self.inOrderHelper(self.root) 

    def inOrderHelper(self, root):

        if not root:
            return 

        self.inOrderHelper(root.left) 

        print(str(root.val) + " ") 

        self.inOrderHelper(root.right) 

class Solution:

    def buildMaxTree(self, nums):

        if not nums:
            return None 

        return self.buildMaxTreeHelper(nums, 0, len(nums) - 1)

    def buildMaxTreeHelper(self, nums, start, end):

        if start > end:

            return None 

        # if start == end:
            
        #     return TreeNode(nums[start]) 

        max_val = max(nums[start : end + 1]) 
        max_index = nums.index(max_val) 

        root = TreeNode(max_val) 

        root.left = self.buildMaxTreeHelper(nums, start, max_index - 1)
        root.right = self.buildMaxTreeHelper(nums, max_index + 1, end) 

        return root 

nums = [3, 2, 1, 6, 0, 1]

solution = Solution()

tree = Tree(solution.buildMaxTree(nums)) 

tree.inOrder() 