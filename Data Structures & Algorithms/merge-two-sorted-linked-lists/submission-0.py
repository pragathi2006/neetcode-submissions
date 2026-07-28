# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=list1
        temp2=list2
        output=ListNode(0)
        temp=output
        a=temp
        while temp1!=None and temp2!=None:
            if temp1.val<=temp2.val:
                temp.next=temp1
                temp1=temp1.next
            else:
                temp.next=temp2
                temp2=temp2.next
            temp=temp.next        

        while temp1!=None:
            temp.next=temp1
            temp=temp.next
            temp1=temp1.next
        while temp2!=None:
            temp.next=temp2
            temp=temp.next
            temp2=temp2.next
        return a.next


