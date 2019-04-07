from heapq import heappush, heappop
'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        
        id_to_highFive = dict()
        
        id_to_avg = dict()
        
        for result in results:
            
            if result.id not in id_to_highFive:
                
                id_to_highFive[result.id] = [] 
                
            heappush(id_to_highFive[result.id], result.score)
            
            if len(id_to_highFive[result.id]) > 5:
                
                heappop(id_to_highFive[result.id])
                
            id_to_avg[result.id] = sum(id_to_highFive[result.id]) / len(id_to_highFive[result.id])
            
        return id_to_avg