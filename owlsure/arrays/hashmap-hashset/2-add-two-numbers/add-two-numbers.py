# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=l1
        temp2=l2
        carry=0
        dummy = ListNode(-1)
        current=dummy

        while(temp1!=None or temp2!=None):
            sum=carry
            if(temp1!=None):
                sum=sum+temp1.val
                temp1 = temp1.next
            if(temp2!=None):
                sum=sum+temp2.val
                temp2 = temp2.next
            
            current.next = ListNode(sum%10)
            carry=sum//10
            current=current.next
        if(carry!=0):
            current.next=ListNode(carry)
        return dummy.next

        