class TreeNode:
    
    def __init__(self, val): 
        
        self.val = val
        
        self.left = None
        
        self.right = None

class Solution:
    
    def inorder(self, root):
        
        if not root:
            
            return [] 
        
        stack = self.buildStack(root) 
        
        results = [] 
        
        while stack:
            
            results.append(stack[-1].val) 
            
            self.moveUpper(stack)
            
        return results
    
    def inorder2(self, root):
        
        curr = root
        
        res = []
        
        pre = None
        
        while curr is not None:
            
            if cur.left is not None: 
                
               pre = curr.left
            
               while pre.right is not None:
                    
                    pre = pre.right
                    
              
               pre.right = cur
             
               temp = cur
            
               cur = cur.left
                
               temp.left = cur
            
            else:
                
               res.append(curr)
            
               cur = cur.right
                
                
        return res
          
               
         
        
    def buildStack(self, root): 
        
        stack = [] 
        
        while root: 
            
            stack.append(root)
            
            root = root.left
            
        return stack
    
    def moveUpper(self, stack): 
        
        node = stack[-1] 
        
        if node.right == None:
            
            node = stack.pop() 
            
            while stack and stack[-1].right == node:
                
                node = stack.pop() 
                
        else: 
            
            node = node.right
            
            while node:
                
                stack.append(node) 
                
                node = node.left