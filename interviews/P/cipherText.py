class Solution:

    def __init__(self, msg, shift):

        self.msg = msg
        # self.shift = shift
        self.encpt = self.encrypt(msg, shift)

    def encrypt(self, msg, shift):
        
        encpt = ""

        i = 0

        while i < len(msg):
            
            c = msg[i]

            if not c.isalpha() and not c.isdigit():

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

                shift += int(c)

                encpt += c  

                i += 1 

        return encpt

solution = Solution("he2l9lo wo1rld@", 3)

print("msg: ", solution.msg)
print("msg: ", solution.encpt)

