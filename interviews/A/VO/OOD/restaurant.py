class Party:

    def __init__(self, capacity):
        self.capacity = capacity 

    def getCapacity(self):
        return self.capacity 

class Table:

    def __init__(self, capacity):
        self.capacity = capacity 
        self.available = True 

    def markUnavailable(self):
        self.isAvailable = False 
        
    def markAvailable(self):
        self.isAvailable = True 

    def getCapacity(self):
        return self.capacity 

    def tableIsAvailable(self):
        return self.available 

class Order:

    def __init__(self, meals, table, party):
        self.meals = meals 
        self.table = table 
        self.party = party 

    def getPrice(self):

        price = 0 

        for meal in self.meals:
            price += meal.getPrice()

        return price 

    def getTable(self):
        return self.table 
    
    def getParty(self):
        return self.party 

class Meal:

    def __init__(self, price):
        self.price = price 
        
    def get_price(self):
        return self.price 

class TimePeroid:

    def __init__(self, start, end):
        self.start = start 
        self.end = end 

class Reservation:
    
    def __init__(self, table, timePeroid):
        self.table = table 
        self.timePeroid = timePeroid

class Restaurant:

    def __init__(self, tables, menu):

        self.tables = tables 
        self.menu = menu 
        self.orders = { table : [] for table in self.tables }

    def findTable(self, party):

        for table in self.tables:

            if table.tableIsAvailable() and table.capacity >= party.getCapacity():
                return table 

        return "NOTABLE"

    def takeOrder(self, order):

        table = order.getTable()

        self.orders[table].append(order)

        table.markUnavailable()

    def checkOut(self, order):

        price = order.getPrice()
        print(price)

        tabel = order.getTable()

        tabel.markAvailable()


        

    






