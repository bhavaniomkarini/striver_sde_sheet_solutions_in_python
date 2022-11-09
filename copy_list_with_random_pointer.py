"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        #step 1 
        
        itr = head
        front = head
        while itr != None:
            front = itr.next
            copy = Node(itr.val)
            itr.next = copy
            copy.next = front
            itr = front
            
        #step 2
        
        itr = head 
        while itr != None:
            if itr.random != None:
                itr.next.random = itr.random.next
            itr = itr.next.next
        
        #step 3
        
        itr = head
        pseudohead = Node(0)
        copy = pseudohead
        while itr != None:
            front = itr.next.next
            copy.next = itr.next
            itr.next = front
            copy = copy.next
            itr = itr.next
            
        return pseudohead.next
        
