# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        if slow==None:
            return False
        if slow.next==None:
            return False
        if fast.next.next==None:
            return False    
        fast=fast.next.next    
        while slow!=None and fast!=None:
            if fast==slow:
                return True  
            slow=slow.next
            if fast.next==None or fast.next.next==None:
                return False
            fast=fast.next.next         
        return False    

        