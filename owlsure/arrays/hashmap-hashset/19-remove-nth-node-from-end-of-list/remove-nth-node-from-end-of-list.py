# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head

        #get the length of list
        while(temp!=None):
            count+=1
            temp=temp.next
        pos = count-n
        temp = head

       

        if temp==None:
            return None
        if pos==0:
            delete = temp
            temp=temp.next
            del delete
            return temp
        k=0
        while temp!=None:
            if(k==pos-1):
                delete = temp.next
                temp.next = temp.next.next
                del delete
                return head
            temp=temp.next
            k+=1
        return head

        