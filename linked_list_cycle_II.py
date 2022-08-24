# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        #edge cases
        
        if head == None or head.next == None:
            return None
        
        slow = head
        fast = head
        entry = head
        
        #finding the collision point of slow and fast pointers
        
        while fast.next != None and fast.next.next != None:
            
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast: # this implies there is a cycle
                
                while slow != entry:
                   
                #finding out the entry of the loop
                
                    slow = slow.next
                    entry = entry.next
                    
                return entry
            
        return None
        
