from collections import deque 

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
        
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        
        if not root:
            return ""
        
        preorder = []
        self.preorderTraverse(root, preorder)
        
        print(",".join(preorder))
        
        return ",".join(preorder)  
        
    def preorderTraverse(self, root, preorder):
        
        if not root:
            return 
        
        preorder.append(str(root.val))
        
        for child in root.children:
            self.preorderTraverse(child, preorder)
        
        preorder.append('#')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        
        if not data:
            return None 
        
        tokens = deque(data.split(','))
        
        return self.helper(tokens)
    
    def helper(self, tokens):
        
        if not tokens:
            return None 
        
        parent = Node(int(tokens.popleft()), [])
        
        while tokens[0] != '#':
            parent.children.append(self.helper(tokens))
            
        tokens.popleft()
        
        return parent 