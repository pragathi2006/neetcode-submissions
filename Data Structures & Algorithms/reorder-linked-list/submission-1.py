# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast=head
        slow=head
      
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        a=slow.next 
        slow.next=None 
        prev=None
        while a!=None:
            cur=a.next
            a.next=prev
            prev=a
            a=cur
        temp1=head
        temp2=prev
        while temp1!=None and temp2!=None:
            next1=temp1.next
            next2=temp2.next
            temp1.next=temp2

            temp2.next=next1
            temp1=next1
            temp2=next2
        return    


            




            

        