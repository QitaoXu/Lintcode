from heapq import heappush, heappop
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        
        heap = [] 
        
        for point in points:
            
            dis = self.get_distance(origin, point)
            
            heappush(heap, (-dis, -point.x, -point.y))
            
            if len(heap) > k:
                
                heappop(heap)
                
        results = []
                
        while heap:
            
            _, x, y = heappop(heap)
            
            results.append(Point(-x, -y))
            
        results.reverse()
        
        return results 
        
    def get_distance(self, p1, p2):
        
        return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 
            
            
