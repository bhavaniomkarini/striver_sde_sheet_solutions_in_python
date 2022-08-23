# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        #defining the reverse function
        def reverseList(head):
            pre = None
            nex = None
            
            while head != None:
                nex = head.next
                head.next = pre
                pre = head
                head = nex
            
            return pre
                
        ListNode.method = reverseList 
            
        
        if head == None or head.next == None:
            return True
        
        #finding the middle of the linked list
        
        slow = head
        fast = head
        
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            
            
        #reversing the linked list 
        #calling the function that we have written
        
        slow.next = reverseList(slow.next)
        
        #moving the slow pointer one step ahead
        
        slow = slow.next
        
        #now iterating the head and slow pointer and checking if the data is equal
        
        while(slow != None):
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        return True
    
      
