DIGIT = {
    0 : "",
    1 : "One",
    2 : "Two",
    3 : "Three",
    4 : "Four",
    5 : "Five",
    6 : "Six",
    7 : "Seven",
    8 : "Eight",
    9 : "Nine"
}

GROUP_TO_WORD = {
    0 : "",
    1 : "Thousand",
    2 : "Million",
    3 : "Billion",
    4 : "Trillion"
}

TWO_LESS_THAN_TWENTY = {
    10 : "Ten",
    11 : "Eleven",
    12 : "Twelve",
    13 : "Thirteen",
    14 : "Fourteen",
    15 : "Fifteen",
    16 : "Sixteen",
    17 : "Seventeen",
    18 : "Eighteen",
    19 : "Nineteen"
}

TEN = {
    0 : "",
    2 : "Twenty",
    3 : "Thirty",
    4 : "Forty",
    5 : "Fifty",
    6 : "Sixty",
    7 : "Seventy",
    8 : "Eighty", 
    9 : "Ninety"
}

class Solution:
    def numberToWords(self, num: int) -> str:
        
        if num == 0:
            
            return "Zero"
        
        digits = self.num_to_digits(num)
        
        digits_groups = [] 
        
        digits_groups_num = (len(digits) - 1) // 3 + 1 
        
        for i in range(0, len(digits), 3):
            
            if i + 3 >= len(digits):
                
                digits_group = digits[i : ]
                
                digits_group.reverse()
                
                digits_groups.append(digits_group)
                
                break
                
            digits_group = digits[i : i + 3]
            
            digits_group.reverse()
            
            digits_groups.append(digits_group)
            
        digits_groups.reverse()
        
        string = ""
        
        strings = []
        
        for digits_group in digits_groups:
            
            string = self.three_digits_to_word(digits_group)
            
            if len(string) != 0:  
                
                strings.append(string)
            
            if digits_groups_num - 1 != 0 and self.digits_to_value(digits_group) != 0:
                
                    strings.append(GROUP_TO_WORD[digits_groups_num - 1])
            
            digits_groups_num -= 1 
            
        return " ".join(strings)
            
        
        
    def num_to_digits(self, num):
        
        digits = [] 
        
        while num > 0:
            
            digit = num % 10 
            
            digits.append(digit)
            
            num = num // 10 
            
        # digits.reverse()
        
        return digits
        
    
        
    #[1, 2, 3] => "One Hunderd Twenty Three"   
    def three_digits_to_word(self, digits):
        
        if len(digits) == 1:
            
            return DIGIT[digits[0]]
        
        if len(digits) == 2:
            
            if digits[0] == 1:
                
                return TWO_LESS_THAN_TWENTY[ digits[0] * 10 + digits[1] ]
            
            else:
                
                if digits[0] == 0 and digits[1] == 0:
                    
                    return ""
                
                elif digits[0] == 0 and digits[1] != 0:
                    
                    return DIGIT[digits[1]]
                
                elif digits[0] != 0 and digits[1] == 0:
                    
                    return TEN[digits[0]]
                
                else:
                    
                    return TEN[digits[0]] + " " + DIGIT[digits[1]]
            
        if len(digits) == 3:
            
            if digits[0] == 0 and digits[1] == 0 and digits[2] == 0:
                
                return ""
            
            if digits[0] == 0 and digits[1] == 0 and digits[2] != 0:
                
                return DIGIT[digits[2]]
            
            if digits[0] == 0 and digits[1] != 0 and digits[2] == 0:
                
                return self.three_digits_to_word(digits[1 : 3])
            
            post_fix = self.three_digits_to_word(digits[1 : 3])
            
            if len(post_fix) == 0:
                
                return DIGIT[digits[0]] + " Hundred"
            
            else:
                
                if digits[0] == 0:
                    
                    return post_fix 
                
                return DIGIT[digits[0]] + " Hundred " + post_fix        
    
    def digits_to_value(self, digits):
        
        value = 0 
        
        for digit in digits:
            
            value = value * 10 + digit
            
        
        return value 