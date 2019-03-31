class Solution:

    def __init__(self, msg, shift):

        self.msg = msg
        self.shift = shift
        self.is_reverse = False 
        self.shift_stack = []
        # self.shift_stack.append(shift)
        self.encpt = self.encrypt(msg, shift)
        
    def encrypt(self, msg, shift):
        
        encpt = ""

        i = 0

        while i < len(msg):

            c = msg[i]

            if not c.isalpha() and not c.isdigit() and c != '-':

                if c == '!':

                    self.is_reverse = not self.is_reverse

                if c == '(':

                    self.shift_stack.append(shift)

                if c == ')':

                    shift = self.shift_stack.pop()

                encpt += c 

                i += 1

                continue 


            if c.isalpha():

                if self.is_reverse == False: # not in reverse mode
                    if c.islower():

                        c = chr( (ord(c) + shift - ord('a')) % 26 + ord('a')  )

                    else:

                        c = chr( (ord(c) + shift - ord('A')) % 26 + ord('A')  )

                else:
                    if c.islower():

                          
                        temp = 25 - (ord(c) + shift - ord('a')) % 26
                        c = chr(temp + ord('a'))

                    else:

                       
                        temp = 25 - (ord(c) + shift - ord('A')) % 26
                        c = chr(temp + ord('A'))

                encpt += c 

                i += 1 

                continue  

            if c.isdigit():

                n = 0

                while c.isdigit():

                    encpt += c 

                    n = n * 10 + int(c)

                    c = msg[i + 1]

                    i = i + 1 

                shift += n 

                continue 

            if c == '-':

                m = 0

                encpt += c

                c = msg[i + 1]

                i += 1 

                while c.isdigit():

                    encpt += c 

                    m = m * 10 + int(c)

                    c = msg[i + 1]

                    i = i + 1 

                shift -= m

                continue 


        return encpt

solution = Solution("he12(!l(9lo w)o!-1r)ld", 30)

print("msg: ", solution.msg)
print("msg: ", solution.encpt)