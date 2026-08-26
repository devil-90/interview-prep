# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        temp1 = list1
        temp2 = list2
        current_node = dummy
        
        while(temp1!=None and temp2!=None):
            if(temp1.val <= temp2.val):
                current_node.next = temp1
                temp1 = temp1.next
            else:
                current_node.next = temp2
                temp2 = temp2.next
            current_node = current_node.next
        
        if(temp1 != None):
            current_node.next = temp1
        if(temp2!=None):
            current_node.next = temp2
        return dummy.next
        