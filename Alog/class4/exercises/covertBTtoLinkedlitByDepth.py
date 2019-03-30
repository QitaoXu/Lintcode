from collections import deque

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        result = []
        queue = deque()
        
        if not root:
            return result 
            
        queue.append(root)
        
        while queue:
            
            size = len(queue)
            
            level_tail = ListNode(-1)
            level_head = level_tail
            
            for _ in range(size):
                
                node = queue.popleft() 
                
                # add a new node in current level linked list
                list_node = ListNode(node.val)
                level_tail.next = list_node
                level_tail = level_tail.next 
                
                for neighbor in [node.left, node.right]:
                    
                    if neighbor != None:
                        
                        queue.append(neighbor)
                        
            result.append(level_head.next)
            
        return result
            
                
            
        