class Solution:
    """
    @param path: the original path
    @return: the simplified path
    """
    def simplifyPath(self, path):
        # write your code here
        
        directorys = path.split("/")
        
        stack = [] 
        
        for directory in directorys:
            
            if directory == ".":
                
                continue 
            
            elif directory == "..":
                
                if stack: # deal with "/../"
                    
                    stack.pop()
                    
            elif directory == "": # deal with "/home//foo/"
                
                continue 
                    
            else:
                
                stack.append(directory)
        
        if not stack: # root directory 
            
            return "/"
            
        elif len(stack) == 1: # subdirectory of root directory 
            
            return "/" + stack[0]
            
        else: # general case 
            
            return "/" + "/".join(stack)
