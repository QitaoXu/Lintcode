from heapq import heappush, heappop
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

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
            
            dis = self.getDistance(origin, point)
            
            heappush(heap, (-dis, -point.x, -point.y))
            
            if len(heap) > k:
                
                heappop(heap)
        
        results = [] 
        
        while heap:
            
            _, x, y = heappop(heap)
            
            results.append(Point(-x, -y))
            
        results.reverse()
        
        return results
        
        
    def getDistance(self, a, b):
        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2