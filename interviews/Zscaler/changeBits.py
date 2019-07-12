class Solution:

    def changeBits(self, num):

        bits = self.num_to_bits(num) 

        modified_bits = self.modify_bits(bits) 

        modified_num = self.bits_to_num(modified_bits) 

        return modified_num 

    def num_to_bits(self, num):

        bits = [] 

        if num == 0:
            return [0, 0] 

        while num > 0:

            bit = num % 2 

            bits.append(bit) 

            num = num // 2 

        if len(bits) % 2 == 1:
            bits.append(0) 

        bits.reverse() 

        return bits 

    def modify_bits(self, bits):

        n = len(bits) 

        for i in range(0, n - 1, 2):

            bits[i], bits[i + 1] = bits[i + 1], bits[i] 

        return bits 

    def bits_to_num(self, bits):

        num = 0 

        for bit in bits:

            num = num * 2 + bit 

        return num 

solution = Solution() 

num = 23 

print(solution.changeBits(num)) 