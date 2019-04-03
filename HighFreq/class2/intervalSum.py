class SegmentNode:
    
    def __init__(self, start, end, val):
        
        self.start = start
        self.end = end 
        self.val = val 
        self.left = None 
        self.right = None 
        
class SegmentTree:
    
    def __init__(self, A):
        
        self.root = self.build(A)
        
    def build(self, A):
        
        return self.build_helper(A, 0, len(A) - 1)
        
    def build_helper(self, A, start, end):
        
        if start > end:
            
            return None 
            
        if start == end:
            
            return SegmentNode(start, end, A[start])
            
        node = SegmentNode(start, end, 0)
        
        mid = (start + end) // 2 
        
        node.left = self.build_helper(A, start, mid)
        node.right = self.build_helper(A, mid + 1, end)
        
        if node.left:
            
            node.val += node.left.val 
            
        if node.right:
            
            node.val += node.right.val 
            
        return node 
        
    def modify(self, root, index, val):
        
        if root.start == root.end and root.start == index:
            
            root.val = val 
            
            return 
        
        mid = (root.start + root.end) // 2 
        
        if index <= mid:
            
            self.modify(root.left, index, val)
            
            root.val = root.left.val + root.right.val 
            
        else:
            
            self.modify(root.right, index, val)
            
            root.val = root.left.val + root.right.val 
            
        
        
    def query(self, root, start, end):
        
        if start <= root.start and root.end <= end:
            
            return root.val 
            
        if start > root.end or end < root.start:
            
            return 0 
            
        return self.query(root.left, start, end) + self.query(root.right, start, end)
        
        
        
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param A: An integer list
    @param queries: An query list
    @return: The result list
    """
    def intervalSum(self, A, queries):
        # write your code here
        
        if not A:
            
            return []
        
        tree = SegmentTree(A)
        
        root = tree.root
        
        res = []
        
        for query in queries:
            
            res.append(tree.query(root, query.start, query.end))
            
        return res