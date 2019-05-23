class Solution:

    def mergeString(self, string1, string2):

        isString1 = True 

        i, j = 0, 0 

        string = ""

        while i < len(string1) and j < len(string2):

            if isString1:

                string += string1[i]
                i += 1 

                isString1 = not isString1

            else:
                string += string2[j]
                j += 1 

                isString1 = not isString1

        if i < len(string1):
            string += string1[i:]

        if j < len(string2):
            string += string2[j:]

        return string 

string1 = "abc"
string2 = "stuvwx"

solution = Solution()
print(solution.mergeString(string1, string2))