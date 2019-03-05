from collections import deque
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        indegrees = {x : 0 for x in range(numCourses)}
        pre_post = {x : [] for x in range(numCourses)}
        
        for post, pre in prerequisites:
            indegrees[post] += 1 
            pre_post[pre].append(post)
        
        start_courses = [ x for x in indegrees.keys() if indegrees[x] == 0]
        queue = deque(start_courses) 
        
        count = 0 
        order = []
        
        while queue:
            
            course = queue.popleft()
            # count += 1
            order.append(course)
            
            for post in pre_post[course]:
                indegrees[post] -= 1 
                if indegrees[post] == 0:
                    queue.append(post)
                    
        return len(order) == numCourses
            