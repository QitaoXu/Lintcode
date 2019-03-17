class Solution:

    def letter(self, string):

        # results = [] 

        if string is None:

            return ""

        hashMap = {}

        for c in string:

            if c not in hashMap:

                hashMap[c] = 1 

            else:

                hashMap[c] += 1 

        nums = []

        for key in hashMap.keys():
            nums.append((key, hashMap[key]))

        # temp = [('a', 0)] * len(nums)

        # self.mergeSort(nums, 0, len(nums) - 1, temp)

        nums = sorted(nums, key = lambda x:x[1], reverse = True)

        for char, value in nums:
            string = "%s:%d;" % (char, value)
            print(string, end="")


    def mergeSort(self, nums, start, end, temp):
        
        if start >= end: 
            return 
        
        mid = (start + end) // 2 
        
        self.mergeSort(nums, start, mid, temp)
        self.mergeSort(nums, mid + 1, end, temp)
        
        self.merge(nums, start, end, temp)

    def merge(self, nums, start, end, temp):
            
        mid = ( start + end ) // 2 
            
        leftIndex = start 
        rightIndex = mid + 1 
            
        index = leftIndex 
            
        while leftIndex <= mid and rightIndex <= end:
                
            if nums[leftIndex][1] > nums[rightIndex][1]:
                temp[index] = nums[leftIndex]
                index += 1 
                leftIndex += 1 
                    
            elif nums[rightIndex][1] > nums[leftIndex][1]:
                temp[index]  = nums[rightIndex]
                index += 1 
                rightIndex += 1 

            else:
                if ord(nums[leftIndex][0]) < ord(nums[rightIndex][0]):
                    temp[index] = nums[leftIndex]
                    index += 1 
                    leftIndex += 1 

                else:
                    temp[index]  = nums[rightIndex]
                    index += 1 
                    rightIndex += 1 
                    
        while leftIndex <= mid:
            temp[index] = nums[leftIndex]
            index += 1 
            leftIndex += 1 
                
        while rightIndex <= end:
            temp[index] = nums[rightIndex]
            index += 1 
            rightIndex += 1 
                
        for i in range(start, end + 1):
            nums[i] = temp[i]
    
        
        
solution = Solution()

solution.letter("aaAABBBCCCCcccc")
        
