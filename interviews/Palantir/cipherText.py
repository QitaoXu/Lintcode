class Solution:

    def __init__(self, msg, shift):

        self.msg = msg
        self.shift = shift
        self.encpt = self.encrypt(msg, shift)

    def encrypt(self, msg, shift):
        
        encpt = ""

        for i in range(len(msg)):
            
            c = msg[i]

            if c.isalpha():

                if c.islower():

                    c = chr( (ord(c) + shift - ord('a')) % 26 + ord('a')  )

                else:

                    c = chr( (ord(c) + shift - ord('A')) % 26 + ord('A')  )

            if c.isdigit():

                shift += int(c)

            encpt += c  

        return encpt

solution = Solution("he2l9lo wo1rld@", 3)

print("msg: ", solution.msg)
print("msg: ", solution.encpt)

