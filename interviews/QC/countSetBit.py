class Solution:

    def __init__(self):

        self.BitsSetTable = [0 for _ in range(256)]

        for i in range(256):

            self.BitsSetTable[i] = (i & 1) + self.BitsSetTable[i // 2]

    def countSetBits(self, num):

        count = 0 

        while num:

            num = num & (num - 1)

            count += 1 

        return count 

    def lookUp(self, num):

        return self.BitsSetTable[num & 0xFF] + \
                self.BitsSetTable[(num >> 8) & 0xFF] + \
                self.BitsSetTable[(num >> 16) & 0xFF] + \
                self.BitsSetTable[(num >> 24) & 0xFF]  