class Event:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isOverlap(self, other): 

        if self.start < other.end or self.end > other.start:
            return True 

        return False 


class Calendar:

    def __init__(self):
        pass 

    def add(self, start, end):
        pass 

    def cancel(self, start, end): 
        pass 