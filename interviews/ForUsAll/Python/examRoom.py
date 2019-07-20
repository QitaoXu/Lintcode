import bisect
class ExamRoom:

    def __init__(self, N):
        self.N = N
        self.students = []
        

    def seat(self):
        
        student = 0
            
        if self.students:
            dist = self.students[0]
            
            for i, s in enumerate(self.students):
                
                if i:
                    prev = self.students[i - 1]
                    
                    d = (s - prev) // 2
                    
                    if d > dist:
                        dist = d 
                        student = prev + d
                        
            if self.N - 1 - self.students[-1] > dist:
                student = self.N - 1
            
        bisect.insort(self.students, student)
        return student
    
    def leave(self, p):
        self.students.remove(p)
