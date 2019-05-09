class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day 

month_to_days = {1 : 31, 2 : 28, 3 : 31, 
                 4 : 30, 5 : 31, 6 : 30, 
                 7 : 31, 8 : 31, 9 : 30,
                 10 : 31, 11 : 30, 12 : 31}

class Solution:

    def twoDates(self, date1, date2):

        if self.is_leap_year(date1.year):
            month_to_days[2] = 29 
        else:
            month_to_days[2] = 28 

        if date1.month == date2.month:
            return max(date1.day, date2.day) - min(date1.day, date2.day)

        elif abs(date1.month - date2.month) == 1:

            minDate = date1 if date1.month < date2.month else date2
            maxDate = date1 if date1.month > date2.month else date2 

            diff = month_to_days[minDate.month] - minDate.day + maxDate.day 
            return diff 

        else:
            minDate = date1 if date1.month < date2.month else date2
            maxDate = date1 if date1.month > date2.month else date2 

            diff = month_to_days[minDate.month] - minDate.day + month_to_days[minDate.month + 1] + maxDate.day 
            return diff 


    def is_leap_year(self, y):

        if ((y % 4 == 0 and y % 100 != 0) or (y % 400 == 0 and y % 3200 != 0)):
            return True 

        else:
            return False 

date1 = Date(2019, 4, 21)
date2 = Date(2019, 6, 1)

solution = Solution()

print(solution.twoDates(date1, date2))



        