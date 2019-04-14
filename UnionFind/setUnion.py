class UnionFind:
    
    def __init__(self, length):
        
        self.father = {i : i for i in range(length)}
        self.count = length
        
    def union(self, a, b):
        
        a_root = self.find(a)
        b_root = self.find(b)
        
        if a_root == b_root:
            
            return 
        
        self.father[b_root] = a_root
        self.count -= 1 
        
    def find(self, point):
        
        path = [] 
        
        while point != self.father[point]:
            
            path.append(point)
            
            point = self.father[point]
            
        for p in path:
            
            self.father[p] = point 
            
        return point 

class Solution:
    """
    @param sets: Initial set list
    @return: The final number of sets
    """
    def setUnion(self, sets):
        # Write your code here
        
        if not sets:
            
            return 0
        
        
        uf = UnionFind(len(sets))
        
        ele_to_set_index = {}
        
        for set_index in range(len(sets)):
            
            cur_set = sets[set_index]
            
            for ele_index in range(len(cur_set)):
                
                cur_ele = cur_set[ele_index]
                
                if cur_ele in ele_to_set_index:
                    
                    uf.union(set_index, ele_to_set_index[cur_ele])
                    
                else:
                    
                    ele_to_set_index[cur_ele] = set_index
                    
        return uf.count 
        
        
