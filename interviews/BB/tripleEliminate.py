class Solution:

    def iterative_deliminate(self, string):

        stack = [] 
        counter_stack = []
        # counter = 0 

        for c in string:

            if not stack:

                stack.append(c)
                counter_stack.append(1) 

            elif stack[-1] != c:

                stack.append(c)
                counter_stack.append(1)  

            elif stack[-1] == c:

                stack.append(c) 
                counter_stack.append(counter_stack[-1] + 1)

                if counter_stack[-1] == 3:
                    for _ in range(3):
                        stack.pop()
                        counter_stack.pop() 

        return "".join(stack) 


    def recursive_deliminate(self, string):

        return self.helper(string)

    def helper(self, string):

        if len(string) < 3:
            return string 

        for i in range(len(string) - 2):

            if string[i] == string[i + 1] and string[i] == string[i + 2]:

                left = string[:i] 
                right = string[i + 3:] if i + 3 < len(string) else ""

                return self.helper(left + right)

        return string 


solution = Solution()
string = "abbbaac"

print(solution.recursive_deliminate(string) )