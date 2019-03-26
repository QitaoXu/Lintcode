import random

import string 

class passwordGenerator:

    def generator(self, num_lower, num_upper, num_digit, num_password):

        if num_lower + num_upper + num_digit != num_password:

            return None 

        if num_lower < 0 or num_upper < 0 or num_digit < 0 or num_password < 0:

            return None

        results = [] 

        permutation = [] 

        self.dfs(permutation, results, num_lower, num_upper, num_digit, num_password)

        return results[0]

    def dfs(self, permutation, results, num_lower, num_upper, num_digit, num_password):

        if len(permutation) == num_password:

            if num_digit == 0 and num_lower == 0 and num_password == 0:

                results.append("".join(permutation.copy()))

        if num_lower < 0 or num_upper < 0 or num_digit < 0:

            return 

        permutation.append(self.get_lower())

        self.dfs(permutation, results, num_lower - 1, num_upper, num_digit, num_password)

        permutation.pop()


        permutation.append(self.get_upper())

        self.dfs(permutation, results, num_lower, num_upper - 1, num_digit, num_password)

        permutation.pop()

        

        permutation.append(self.get_digit())

        self.dfs(permutation, results, num_lower, num_upper, num_digit - 1, num_password)

        permutation.pop()

        

    def get_digit(self):
        return random.choice("0123456789")


    def get_upper(self):

        return random.choice("abcdefghijklmnopqrstuvwxyz")

    def get_lower(self):

        return random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

