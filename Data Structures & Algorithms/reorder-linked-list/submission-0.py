# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l=[]
        a=ListNode(0)
        temp1=a
        temp=head
        while temp!=None:
            l.append(temp)
            temp=temp.next
        i=0
        j=len(l)-1 
           
        while i<j:
            temp1.next=l[i]
            temp1=temp1.next
            temp1.next=l[j]
            temp1=temp1.next
            i+=1
            j-=1
        if i==j:
            temp1.next=l[i]
            temp1=temp1.next
        temp1.next=None
        return        