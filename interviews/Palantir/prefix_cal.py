class Solution:

    def __init__(self, infix):

        self.infix = infix 
        self.postfix = self.infix_to_postfix(infix)
        self.prefix = self.infix_to_prefix(infix)
        self.result = self.postfix_to_val(self.postfix)

    def is_operator(self, op):

        return not op.isalpha() and not op.isdigit()
    
    def infix_to_postfix(self, infix):

        infix = '(' + infix + ')'

        length = len(infix)

        stack = [] 

        postfix = ""

        for i in range(length):

            if infix[i].isdigit(): # number
                postfix = postfix + infix[i]

            elif infix[i] == '(': # (
                stack.append(infix[i])

            elif infix[i] == ')': # )

                while stack[-1] != '(':

                    postfix = postfix + stack.pop()

                stack.pop()

            else: # operand

                if self.is_operator(stack[-1]):

                    while self.get_priority(infix[i]) \
                        <= self.get_priority(stack[-1]):

                        postfix = postfix + stack.pop()
                    
                    stack.append(infix[i])
        
        return postfix





    def infix_to_prefix(self, infix):

        length = len(infix)

        infix = infix[::-1]

        for i in range(length):

            if infix[i] == '(':

                infix[i] == ')'

            elif infix[i] == ')':

                infix[i] == '('

        prefix = self.infix_to_postfix(infix)

        prefix = prefix[::-1]

        return prefix
    
    def get_priority(self, operator):

        if operator == '+' or operator == '-':

            return 1 

        elif operator == '*' or operator == '/':

            return 2 

        elif operator == '^':

            return 3 

        return 0



    def prefix_to_val(self, prefix):

        stack = []

        for j in range(len(prefix) - 1, -1, -1):

            if prefix[j].isdigit():

                stack.append(prefix[j])

            else:

                o1 = int(stack.pop())
                o2 = int(stack.pop())

                if prefix[j] == '+':

                    stack.append(o1 + o2)

                    continue 

                elif prefix[j] == '-':

                    stack.append(o1 - o2)

                    continue 

                elif prefix[j] == '*':

                    stack.append(o1 * o2)

                    continue 

                else:

                    stack.append(o1 / o2)

                    continue 
        
        return stack[-1]


    def postfix_to_val(self, postfix):

        stack = [] 

        for i in range(len(postfix)):

            if postfix[i] == ' ':

                continue 

            elif postfix[i].isdigit():

                n = 0 

                while postfix[i].isdigit():

                    n = n * 10 + ord(postfix[i]) - ord('0')
                    i += 1 

                i -= 1 

                stack.append(n)

            else:

                o1 = stack.pop()
                o2 = stack.pop()

                if postfix[i] == '+':

                    stack.append(o2 + o1)

                    continue 

                elif postfix[i] == '-':

                    stack.append(o2 - o1)

                    continue 

                elif postfix[i] == '*':

                    stack.append(o2 * o1)

                    continue 

                else:

                    stack.append(o2 / o1)

                    continue 

        return stack[-1]

solution = Solution("3/3+4*5")

print("Infix: ", solution.infix)
print("Postfix: ", solution.postfix)
print("Prefix: ", solution.prefix)
print("value: ", solution.result)

      