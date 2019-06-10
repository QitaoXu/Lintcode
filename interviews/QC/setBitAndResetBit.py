class Solution:

    def setBit(self, num, bit_index):

        bits = [0 for _ in range(32)] 

        bits[bit_index] = 1 

        op_num = 0 

        for bit in bits:

            op_num = op_num * 2 + bit 

        return num | op_num

    def resetBit(self, num, bit_index):

        bits = [1 for _ in range(32)]

        bits[bit_index] = 0 

        op_num = 0 

        for bit in bits:

            op_num = op_num * 2 + bit 

        return num & op_num

