import datetime

class Vehicle:

    def __init__(self):
        self.size = None 
    
    def getSize(self):
        return  self.size 

class VehicleSize:
    MotorCycle = 1 
    Car = 2 
    Bus = 5 

class Car(Vehicle):
    def  __init__(self):
        
        Vehicle.__init__(self)
        self.size = VehicleSize.Car

class MotorCycle(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.size = VehicleSize.MotorCycle

class Bus(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.size = VehicleSize.Bus 

class Ticket:
    def __init__(self, vehicle, spots):

        self.vehcile = vehicle 
        self.spots = spots 
        self.startTime = datetime.datetime.now()

class Level:
    def __init__(self, rows, avaiableCount):
        self.rows = rows 
        self.avaiableCount = 0 
        
        for row in rows:
            self.avaiableCount += len(row.spots)

    def getAvaiableCount(self):
        count = 0 

        for row in self.rows:
            for spot in row.spots:
                count = count + 1 if spot.isAvailable() else count + 0 

        return count 

    def updateAvailableCount(self, diff):
        
        self.avaiableCount += diff 


class Row:
    def __init__(self, spots):
        self.spots = spots 

class Spot:
    def __init__(self, level):
        self.level = level 
        self.avaiable = True 

    def isAvailable(self):
        return self.avaiable 

    def takeSpot(self):
        if not self.isAvailable():
            return 
        
        self.avaiable = False 

    def leaveSpot(self):
        if self.isAvailable():
            return 
        
        self.avaiable = True 

class Exception:
    ParkingFullException = "ParkingFullException"
    InvalidTicketExeception = "InvalidTicketExeception"

class ParkingLot:
    def __init__(self, levels, hourlyRate):
        self.levels = levels
        self.hourlyRate = hourlyRate 

    def getAvaiableCount(self):
        
        count = 0 

        for level in self.levels:
            count += level.getAvaiableCount()

        return count 

    def _findSpotsForVehicle(self, vehicle):
        # return List<Spot> spots

        spots = []
        # Implementation of find algorithm 
        return spots 
    
    def parkVehicle(self, vehicle):
        # return Ticket t 
        spots = self._findSpotsForVehicle(vehicle)

        for spot in spots:
            spot.takeSpot()
            spot.level.updateAvailableCount(-1)

        ticket = Ticket(vehicle, spots)
        
        return ticket 

    def clearSpot(self, ticket):

        price = self._caculatePrice(ticket)

        print(price)

        for spot in ticket.spots:
            spot.leaveSpot()
            spot.level.updateAvailableCount(1)

    def _caculatePrice(self, ticket):
        
        curtTime = datetime.datetime.now()

        timeDiff = (curtTime - ticket.startTime) // 60 
        return timeDiff * self.hourlyRate
        


