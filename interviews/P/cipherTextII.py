class Solution:

    def __init__(self, msg, shift):

        self.msg = msg
        # self.shift = shift
        self.encpt = self.encrypt(msg, shift)
        # self.is_reverse = False 

    def encrypt(self, msg, shift):
        
        encpt = ""

        i = 0

        while i < len(msg):

            c = msg[i]

            if not c.isalpha() and not c.isdigit() and c != '-':

                encpt += c 

                i += 1

                continue 


            if c.isalpha():

                if c.islower():

                    c = chr( (ord(c) + shift - ord('a')) % 26 + ord('a')  )

                else:

                    c = chr( (ord(c) + shift - ord('A')) % 26 + ord('A')  )

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

solution = Solution("he12l9lo wo-1rld", 7)

print("msg: ", solution.msg)
print("msg: ", solution.encpt)