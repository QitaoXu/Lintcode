class Solution:

    def validMultiParenthesis(self, string):

        if not string:
            return True 

        stack = [] 
        parenthesis = set(["(", ")", "[", "]", "{", "}"])
        pair = {")" : "(", "}" : "{", "]" : "["}

        for c in string:

            if c not in parenthesis:
                continue 

            elif c == "(" or c == "[" or c == "{":
                stack.append(c)
                continue 

            else:
                
                if not self.check(c, stack, pair):
                    return False 

        return len(stack) == 0 

    def check(self, c, stack, pair):

        if not stack or stack[-1] != pair[c]:
            return False 

        stack.pop()
        return True 

solution = Solution()

string = "{[9999](){}}"

print(solution.validMultiParenthesis(string))
                    
                


                 

            