class Solution:
    """
    @param num: a non-negative integer
    @return: english words representation
    """
    def __init__(self):
        self.lessThan20 = ["","One","Two","Three","Four","Five",
                            "Six","Seven","Eight","Nine","Ten",
                            "Eleven","Twelve","Thirteen","Fourteen","Fifteen",
                            "Sixteen","Seventeen","Eighteen","Nineteen"]
                            
        self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty",
                        "Sixty","Seventy","Eighty","Ninety"]
                        
        self.thousands = ["","Thousand","Million","Billion"]
        
    def numberToWords(self, num):
        # Write your code here
        
        if num == 0:
            
            return "Zero"
            
        res = ""
        
        for i in range(len(self.thousands)):
            
            if num % 1000 != 0:
                
                res = self.num_to_English(num % 1000) + self.thousands[i] + " " + res
                
            num //= 1000
            
        return res.strip()
     
       
    def num_to_English(self, num):
        
        if num == 0:
            
            return ""
            
        elif num < 20:
            
            return self.lessThan20[num] + " "
            
        elif num < 100:
            
            return self.tens[num // 10] + " " + self.num_to_English(num % 10)
            
        else:
            
            return self.lessThan20[num // 100] + " Hundred " + self.num_to_English(num % 100)
            
            
