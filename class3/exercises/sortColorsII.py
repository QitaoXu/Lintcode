class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        
        if colors == None or len(colors) == 0:
            return 
        nums = colors
        self.quickSort(colors, 1, k, 0, len(nums) - 1)
        
    def quickSort(self, nums, color_from, color_to, index_from, index_to):
        
        if color_from == color_to or index_from == index_to:
            return 
        
        left, right = index_from, index_to
        
        color = (color_from + color_to) // 2   
        
        while left <= right:
            
            while left <= right and nums[left] <= color:
                left += 1 
                
            while left <= right and nums[right] > color:
                right -= 1 
                
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1 
                
        self.quickSort(nums, color_from, color, index_from, right)
        self.quickSort(nums, color + 1, color_to, left, index_to)