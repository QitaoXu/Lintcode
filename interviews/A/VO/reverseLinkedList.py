# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self, nums):
        self.head = ListNode(-1)
        self.tail = self.head 
        self.buildList(nums)

    def buildList(self, nums):

        for num in nums:

            node = ListNode(num)

            self.tail.next = node 
            self.tail = self.tail.next 

    def printList(self):

        node = self.head.next 

        while node: 

            print(str(node.val) + " -> ", end="")
            node = node.next 
        
        print("#")

    def reverseList(self):

        prev = None 
        curr = self.head.next 

        while curr != None:

            nextTemp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = nextTemp

        self.head.next = prev 

    def reverseListByPart(self, start, end):

        prev = start  
        curr = start.next 
        prev_end = start.next 

        while curr != end:

            nextTemp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = nextTemp

        start.next = prev 
        prev_end.next = end 
 

# 1 -> 2 -> 3 -> 4 -> 5 -> 6 
# 1 -> 5 -> 4 -> 3 -> 2 -> 6 

nums = [1, 2, 3]
linked_list = LinkedList(nums)

linked_list.printList()

linked_list.reverseListByPart(linked_list.head.next, linked_list.tail)

linked_list.printList()
        
        
        