class Solution:
    """
    @param L: an integer
    @param R: an integer
    @return: the count of numbers in the range [L, R] having a prime number of set bits in their binary representation
    """
    def countPrimeSetBits(self, L, R):
        # Write your code here
        
        # prime_set = set([2, 3, 5, 7, 11, 13, 17, 19])
        
        count = 0 
        
        for num in range(L, R + 1):
            
            bits = self.num_to_num_set_bits(num)
            
            if self.isPrime(bits):
                
                count += 1 
                
        return count 
        
        
    def num_to_num_set_bits(self, num):
        
        if num == 0:
            
            return 0 
            
        bits = 0 
        
        while num > 0:
            
            if num % 2 == 1:
                
                bits += 1 
                
            num = num // 2 
            
        return bits 
        
    def isPrime(self, num):
        
        if num < 2:
            
            return False 
            
        if num == 2:
            
            return True 
            
        i = 2 
        
        while i ** 2 <= num:
            
            if num % i == 0:
                
                return False 
                
            i += 1 
            
        return True  