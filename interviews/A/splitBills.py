class Solution:

    def splitBills(self, paid, unpaid):

        n = len(paid) + len(unpaid)

        avg = sum(paid.values) / n 

        underpay = [] 
        overpay = [] 

        