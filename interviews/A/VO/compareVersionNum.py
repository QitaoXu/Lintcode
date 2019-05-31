class VersionSegment:

    def __init__(self, string):

        self.num, self.suffix = self.helper(string)

    
    def helper(self, string):

        num = 0 
        suffix = ""

        for i in range(len(string)): 

            if string[i].isdigit():

                num = num * 10 + int(string[i])

            else:

                suffix = string[i:]
                break 

        return num, suffix 

    def __lt__(self, other):

        if self.num == other.num:
            return self.suffix < other.suffix 

        return self.num < other.num 

    def __eq__(self, other):
        return self.num == other.num and self.suffix == other.suffix 

    def __gt__(self, other):

        if self.num == other.num:
            return self.suffix > other.suffix 

        return self.num > other.num 


class Solution:

    def compareVersionNum(self, version1, version2):

        v1_list = version1.split(".")
        v2_list = version2.split(".")

        v1, v2 = [], [] 

        for seg in v1_list:
            v1.append(VersionSegment(seg))
        
        for seq in v2_list:
            v2.append(VersionSegment(seq))

        for i in range( max(len(v1), len(v2)) ): 

            v1_seg = v1[i] if i < len(v1) else VersionSegment("0")
            v2_seg = v2[i] if i < len(v1) else VersionSegment("0")

            if v1_seg > v2_seg:
                return 1 

            elif v1_seg < v2_seg:
                return -1 

            else:
                continue 

        return 0 

solution = Solution()

v1 = "1.1"
v2 = "1.1ab"

print(solution.compareVersionNum(v1, v2))

